from abc import ABC, abstractmethod


class FileProcessor(ABC):
    """
    Mechanisms for processing various types of files
    (for example, images, text files, etc.).
    """

    @abstractmethod
    def process_file(self, file_obj):
        pass


class ImageFileProcessor(FileProcessor):
    def process_file(self, file_obj):
        """
        Process an image file.

        Placeholder function. Actual image processing logic should be implemented here.
        """
        # Placeholder logic for image processing
        print("Image file processed")
        pass


class TextFileProcessor(FileProcessor):
    def process_file(self, file_obj):
        """
        Process a text file.

        Placeholder function. Actual text processing logic should be implemented here.
        """
        print("Text file processed")
        # Placeholder logic for text processing
        pass
