from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Устанавливаем переменную окружения для Celery
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

# Создаем экземпляр объекта Celery
app = Celery("core")

# Загружаем настройки из Django settings.py
app.config_from_object("django.conf:settings", namespace="CELERY")

# Автоматически находим и регистрируем все задачи (tasks) в приложениях Django
app.autodiscover_tasks()
