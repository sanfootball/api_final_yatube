# API для Yatube

API для Yatube — это REST API, который предоставляет возможность создания, чтения, обновления и удаления данных на платформе Yatube.

## Установка и запуск проекта

Для установки и запуска проекта необходимо выполнить следующие шаги:

1. Склонировать репозиторий:

git clone https://github.com/sanfootball/api_final_yatube

2. Перейти в директорию с проектом:

cd api_final_yatube

3. Создать виртуальное окружение и активировать его:

python -m venv venv
source venv/Scripts/activate

4. Установить зависимости:

pip install -r requirements.txt

5. Применить миграции:

python manage.py migrate

6. Запустить сервер:

python manage.py runserver

## Документация API

Документация API доступна по адресу http://localhost:8000/redoc/

## Технологии

* Python 3.9.5
* Django 3.2.4
* Django REST framework 3.12.4
