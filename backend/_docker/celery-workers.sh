#!/bin/sh

WORKERS=${CELERY_WORKERS:=3}
LOG_LEVEL=${CELERY_LOG_LEVEL:=warning}

echo "Starting ${WORKERS} celery workers with ENV=${ENV}."
echo "CI_BUILD_DATE     =${CI_BUILD_DATE}"
echo "CI_COMMIT_SHA     =${CI_COMMIT_SHA}"
echo "CI_COMMIT_REF_SLUG=${CI_COMMIT_REF_SLUG}"

rm -f /var/run/celery*
celery -A cloudlinux worker -l ${LOG_LEVEL} --pidfile=/var/run/celery-worker_${ENV}.pid -c ${WORKERS} "$@"
