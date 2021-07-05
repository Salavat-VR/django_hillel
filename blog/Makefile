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

urls:
	$(MANAGE) show_urls

celery worker:
	celery -A core worker -l info

createsuperuser:
	$(MANAGE) createsuperuser

gunicorn-run:
	gunicorn -w 4 -b 0.0.0.0:$(WSGI_PORT) --chdir /home/dmytro/Desktop/wks/linux_venv/my_1st_django/blog core.wsgi --timeout 30 --log-level debug --max-requests 10000

coverage:
	coverage report --omit */venv/*

tst:
	pytest --cov=main --cov-report=html --cov-fail-under=60

docker-build:
	sudo docker build .

#command for
#run container with name its_my_app and use f20f55700305 image + auto delete after stopping a container
# 8222 - port in host 8000 - port in container
docker-run:
	sudo docker run --rm -t -d -p 8222:8111 --name my_app f20f55700305

#change the name in prod.
docker-stop:
	sudo docker container stop my_app

docker-up:
	docker-compose up -d --build

docker-down:
	docker-compose down

celery-run:
	cd src && celery -A core worker -l info

copy-static:
	# collected static so that we could operate them further
	docker exec -it backend python blog/manage.py collectstatic --noinput
	# copy from backend to our host
	docker cp backend:/tmp/static_content/static /tmp/static
	# copy from our host to nginx to be able manage static
	docker cp /tmp/static nginx:/etc/nginx

# for breakpoint()
docker-runserver-breakpoint:
	docker exec -it backend $(MANAGE) runserver 0.0.0.0:9000