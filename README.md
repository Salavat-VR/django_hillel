in Makefile:

gunicorn-run:
	gunicorn -w 4 -b 0.0.0.0:$(WSGI_PORT) --chdir /home/dmytro/Desktop/wks/linux_venv/my_1st_django/blog core.wsgi --timeout 30 --log-level debug --max-requests 10000


nginx config:

    *have to add*
