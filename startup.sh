#!/bin/sh
python manage.py collectstatic --noinput
python manage.py migrate
gunicorn "scheduler.wsgi" -b "0.0.0.0:${PORT}"