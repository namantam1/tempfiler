#!/bin/bash
NUM_WORKERS=2

export DJANGO_SETTINGS_MODULE=$WORK_DIR.$PROJECT.settings
export DJANGO_WSGI_MODULE=$WORK_DIR.$PROJECT.wsgi


echo $DJANGO_SETTINGS_MODULE
echo "Starting server as $(whoami)"

exec poetry run gunicorn ${DJANGO_WSGI_MODULE}:application \
    --bind 0.0.0.0:8000 --timeout 120 \
    --workers $NUM_WORKERS \
    --log-level=debug \
    --log-file=-
