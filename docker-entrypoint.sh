#!/bin/sh
set -e

if [ ! -z "$DATABASE_URL" ]; then
    until psql $DATABASE_URL -c '\l'; do
      >&2 echo "Postgres is unavailable - sleeping"
      sleep 1
    done
fi

>&2 echo "Postgres is up - continuing"

if [ "x$DJANGO_MANAGEPY_MIGRATE" = 'xon' ]; then
    /venv/bin/python manage.py migrate --noinput
fi

if [ "x$DJANGO_MANAGEPY_COLLECTSTATIC" = 'xon' ]; then
    /venv/bin/python manage.py collectstatic --noinput
fi

# CREATE_SUPER_USER=admin:admin@example.com:password
if [[ -n "$CREATE_SUPER_USER" ]]; then
    echo "==> Creating super user"
    printf "from django.contrib.auth.models import User\nif not User.objects.exists(): User.objects.create_superuser(*'$CREATE_SUPER_USER'.split(':'))" | /venv/bin/python manage.py shell
fi

exec "$@"