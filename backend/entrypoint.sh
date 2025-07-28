#!/bin/sh

echo "Starting Django with ENV=$ENV"

if [ "$ENV" = "prod" ]; then
  echo "Starting Gunicorn server for PRODUCTION"
  # 마이그레이션도 여기서 할 수 있음
  python manage.py migrate
  exec gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 3
elif [ "$ENV" = "local" ]; then
  echo "Starting Django development server (local)"
  python manage.py migrate
  exec python manage.py runserver 0.0.0.0:8000 --settings=config.settings.local
elif [ "$ENV" = "dev" ]; then
  echo "Starting Django development server (dev)"
  python manage.py migrate
  exec python manage.py runserver 0.0.0.0:8000 --settings=config.settings.dev
else
  echo "Assigned an unexpected value in environment variable 'ENV'! Please sets among prod, local, dev."
  exit 0
fi
