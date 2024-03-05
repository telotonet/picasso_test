from django.contrib import admin
from .models import File


class FileAdmin(admin.ModelAdmin):
    list_display = ("upload", "uploaded_at", "processed")
    list_editable = ["processed"]
    list_filter = ["processed"]


admin.site.register(File, FileAdmin)
# Register your models here.
