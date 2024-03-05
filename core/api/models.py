from django.db import models


class File(models.Model):
    upload = models.FileField(upload_to="uploads/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False, verbose_name="Статус обработки")

    def __str__(self):
        return f"{self.upload}"
