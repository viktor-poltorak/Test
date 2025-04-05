#!/bin/bash

echo "Starting JCCloud Django App with ENV=${ENV}."
echo "CI_BUILD_DATE     =${CI_BUILD_DATE}"
echo "CI_COMMIT_SHA     =${CI_COMMIT_SHA}"
echo "CI_COMMIT_REF_SLUG=${CI_COMMIT_REF_SLUG}"

# exit if any command below is failed
set -e
python ./manage.py migrate --no-input
python ./manage.py compilemessages
python ./manage.py collectstatic --noinput

gunicorn \
 --bind 0.0.0.0:8000 \
 --worker-connections=1000 \
 --access-logfile - \
 --error-logfile - \
 --env DJANGO_SETTINGS_MODULE=cloudlinux.settings \
 cloudlinux.asgi:application
