#!/bin/sh
echo "Apply migrations, create super user"
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser --username admin --email test@test.com --noinput


echo "Start gunicorn server"
gunicorn -w 1 config.wsgi:application --bind 0.0.0.0:8000
celery -A config -b "amqp://rabbitmq:5672/vhost" beat --scheduler django_celery_beat.schedulers:DatabaseScheduler
exec "$@"
