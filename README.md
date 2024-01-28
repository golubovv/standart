Инструкция по запуску проекта (windows):

Склонируйте проект:
git clone https://github.com/golubovv/standart.git

Создайте и активируйте виртуальное оркужение:
python -m venv venv
venv\scripts\activate

Установите зависимости:
pip install -r requirements.txt

Создайте и заполните .env файл по шаблону:
SECRET_KEY = Секретный ключ. Например: django-insecure-d5$9*-3ym6b_2u5$s5bf_(6jfm4zuykqtsk+6u*q&sm198/&3a
DATABASE = Имя вашей базы данных
USER = Имя пользователя
PASSWORD = Пароль от пользователя
DB_HOST = Хост базы данных (localhost)
DB_PORT = Порт базы данных (5432 по умолчанию)

Примените миграции:
python manage.py migrate

Заполните базу данных тестовыми значениями:
python manage.py filldb

Всё готовов, можете запускать проект:
python manage.py runserver
