### Run devenv

`docker compose up db redis`

`cd ./backend && ./manage.py runserver 0.0.0.0:8000`

`celery -A cloudlinux beat --loglevel=INFO`
`celery -A cloudlinux worker --loglevel=INFO`

`cd ./frontend && yarn dev`