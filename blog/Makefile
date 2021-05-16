MANAGE = python manage.py
WSGI_PORT = 8081

run:
	$(MANAGE) runserver


make_migrations:
	$(MANAGE) makemigrations


migrate:
	$(MANAGE) migrate

shell_plus:
	$(MANAGE) shell_plus --print-sql

celery worker:
	celery -A blog worker -l info


celery worker:
	celery -A blog beat -l info

createsuperuser:
	$(MANAGE) createsuperuser

gunicorn-run:
	gunicorn -w 4 -b 0.0.0.0:8081 --chdir blog core.wsgi --timeout 30 --log-level debug --max-request 10000

collect-static:
	$(MANAGE) collectstatic