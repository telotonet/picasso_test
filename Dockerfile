FROM python:3.12

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./core/requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt --no-cache-dir

COPY . /usr/src/app/