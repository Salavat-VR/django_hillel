run:
	python manage.py runserver


make_migrations:
	python manage.py makemigrations


migrate:
	python manage.py migrate

shell_plus:
	python manage.py shell_plus --print-sql

celery worker:
	celery -A blog worker -l info


celery worker:
	celery -A blog beat -l info