# Il-Forno

как запустить проект

Сначала скачайте проект на компьютер и перейдите в папку проекта
далее

python -m venv env
.\env\Scripts\activate
pip install django
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver