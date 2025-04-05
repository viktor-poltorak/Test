#!/bin/sh

echo "Starting celery beat with ENV=${ENV}."
echo "CI_BUILD_DATE     =${CI_BUILD_DATE}"
echo "CI_COMMIT_SHA     =${CI_COMMIT_SHA}"
echo "CI_COMMIT_REF_SLUG=${CI_COMMIT_REF_SLUG}"
rm -f /var/run/celery*
celery -A cloudlinux beat -l info \
    --schedule=/var/run/beat-schedule_${ENV} \
    --pidfile=/var/run/celery-beat_${ENV}.pid
