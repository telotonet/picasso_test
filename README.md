# Загрузка и обработка файлов

Этот проект разработан для реализации Django REST API, который позволяет загружать файлы на сервер и асинхронно обрабатывать их с использованием Celery.

## Требования

Прежде чем начать работу с проектом, убедитесь, что у вас установлены следующие компоненты:

- Docker
- Docker Compose

## Установка

1. Клонируйте репозиторий на свой локальный компьютер:

```bash
git clone https://github.com/your_username/project_name.git
cd project_name
```

2. Скопируйте файл `.env.example` в файл `.env`:

```bash
cp .env.example .env
```

3. Запустите Docker Compose для сборки и запуска контейнеров:

```bash
docker-compose up --build
```

4. Примените миграции к базе данных:

```bash
docker-compose exec django python manage.py migrate
```

## Использование

### Загрузка файлов

Для загрузки файлов на сервер используйте API-эндпоинт `upload/`. Отправьте POST-запрос с файлом в поле `file`. Пример использования с помощью cURL:

```bash
curl -X POST -F "file=@/path/to/your/file.jpg" http://localhost:8000/api/upload/
```

### Получение списка файлов

Чтобы получить список всех файлов с их данными, включая статус обработки, используйте API-эндпоинт `files/`. Пример использования с помощью cURL:

```bash
curl http://localhost:8000/api/files/
```
