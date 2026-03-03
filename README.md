# E5041.pro — Комбинация Metal + Liquid 3D

Запуск:
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env
python manage.py migrate
python manage.py runserver