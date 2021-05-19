MANAGE = python manage.py
WSGI_PORT = 8081

run:
	$(MANAGE) runserver

collect-static:
	$(MANAGE) collectstatic

make_migrations:
	$(MANAGE) makemigrations

migrations_dry:
	$(MANAGE)  makemigrations --check --dry-run

migrate:
	$(MANAGE) migrate

shell_plus:
	$(MANAGE) shell_plus --print-sql

celery worker:
	celery -A blog worker -l info

createsuperuser:
	$(MANAGE) createsuperuser

gunicorn-run:
	gunicorn -w 4 -b 0.0.0.0:$(WSGI_PORT) --chdir /home/dmytro/Desktop/wks/linux_venv/my_1st_django/blog core.wsgi --timeout 30 --log-level debug --max-requests 10000
