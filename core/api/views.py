from rest_framework.generics import ListAPIView, CreateAPIView
from .models import File
from .serializers import FileSerializer
from .tasks import process_file


class FileUploadView(CreateAPIView):
    """
    API endpoint to upload files.

    This view handles file uploads and triggers an asynchronous task
    to process the uploaded file.
    """

    serializer_class = FileSerializer

    def perform_create(self, serializer):
        """
        Perform additional actions after creating a new file object.
        This method triggers an asynchronous task to process the file.
        """
        file_obj = serializer.save()
        process_file.delay(file_obj.id)


class FileListView(ListAPIView):
    """
    API endpoint to list all files.

    This view returns a list of all files stored in the database.
    """

    queryset = File.objects.all()
    serializer_class = FileSerializer
