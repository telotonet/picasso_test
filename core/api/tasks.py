from celery import shared_task
from .models import File
from .file_processors import ImageFileProcessor, TextFileProcessor
import os
import logging

logger = logging.getLogger(__name__)


FILE_PROCESSORS = {
    ".txt": TextFileProcessor(),
    ".png": ImageFileProcessor(),
    # Add more mappings for other file types if needed
}


@shared_task
def process_file(file_id):
    """
    Celery task to process a file asynchronously.

    Determines the type of file and processesit
    accordingly using the appropriate file processor.
    """
    try:
        file_obj = File.objects.get(pk=file_id)
        print(file_obj.upload)
        if not file_obj.processed:
            # Determine the type of file and process accordingly
            file_extension = os.path.splitext(file_obj.upload.name)[1]
            file_processor = get_file_processor(file_extension)
            if not file_processor:
                logger.warning(
                    f"Unsupported file type '{file_extension}' for file ID {file_id}. Skipping processing."
                )
                return
            file_processor.process_file(file_obj)
            file_obj.processed = True
            file_obj.save()

    except File.DoesNotExist:
        logger.error(f"File with ID {file_id} does not exist.")

    except Exception as e:
        logger.exception(f"An error occurred while processing file ID {file_id}: {e}")


def get_file_processor(file_extension):
    return FILE_PROCESSORS.get(file_extension)
