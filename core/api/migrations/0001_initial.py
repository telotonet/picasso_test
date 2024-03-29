# Generated by Django 5.0.2 on 2024-02-26 07:25

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="File",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("upload", models.FileField(upload_to="uploads/")),
                ("uploaded_at", models.DateTimeField(auto_now_add=True)),
                (
                    "processed",
                    models.BooleanField(default=False, verbose_name="Статус обработки"),
                ),
            ],
            options={
                "verbose_name": "Файл",
                "verbose_name_plural": "Файлы",
            },
        ),
    ]
