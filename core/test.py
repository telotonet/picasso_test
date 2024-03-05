from locust import HttpUser, task, between
from django.core.files.uploadedfile import SimpleUploadedFile



class FileUploadUser(HttpUser):
    wait_time = between(5, 9)

    @task
    def upload_file(self):
        uploaded_file = SimpleUploadedFile("test_file.txt", b"Test file content")
        self.client.post("/upload/", {"upload": uploaded_file})

class FileListUser(HttpUser):
    wait_time = between(5, 9)

    @task
    def list_files(self):
        self.client.get("/files/")