release: python manage.py makemigrations
release: python manage.py migrate
release: python manage.py collectstatic

web: gunicorn demo.wsgi --log-file -