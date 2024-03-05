from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.test import TestCase, override_settings
from django.core.files.uploadedfile import SimpleUploadedFile
import shutil, tempfile, os
from .models import File
from .tasks import process_file

MEDIA_ROOT = tempfile.mkdtemp()

@override_settings(MEDIA_ROOT=MEDIA_ROOT)
class FileUploadTestCase(APITestCase):

    @classmethod
    def tearDownClass(cls): 
        shutil.rmtree(MEDIA_ROOT, ignore_errors=True)
        super().tearDownClass()

    def setUp(self):
        self.url = reverse("file-create")
        self.uploaded_file = SimpleUploadedFile("test_file.txt", b"Test file content")

    def test_file_upload(self):
        data = {"upload": self.uploaded_file}
        response = self.client.post(self.url, data, format="multipart")

        # Проверяем ответ на корректность
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue("id" in response.data)
        self.assertTrue("upload" in response.data)
        self.assertTrue("uploaded_at" in response.data)
        self.assertTrue("processed" in response.data)
        self.file_id = response.data["id"]
        self.assertTrue(File.objects.filter(id=self.file_id).exists())


class FileListTestCase(APITestCase):
    multi_db = True
    def setUp(self):
        self.url = reverse("file-list")
        self.file = File.objects.create(upload="test_file.txt", processed=True)

    def test_file_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["id"], self.file.id)
        self.assertEqual(
            os.path.basename(response.data[0]["upload"]),
            os.path.basename(self.file.upload.url),
        )
        self.assertEqual(response.data[0]["processed"], self.file.processed)


class FileProcessingTestCase(TestCase):
    multi_db = True
    def test_process_file_task(self):
        file = File.objects.create(upload="test_file.txt", processed=False)
        process_file(file.id)
        file.refresh_from_db()
        self.assertTrue(file.processed)
