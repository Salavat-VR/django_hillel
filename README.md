in Makefile:

gunicorn-run:
	gunicorn -w 4 -b 0.0.0.0:$(WSGI_PORT) --chdir /home/dmytro/Desktop/wks/linux_venv/my_1st_django/blog core.wsgi --timeout 30 --log-level debug --max-requests 10000


nginx config:
    
    server {
    listen 80;
    listen [::]:80
    server_name 127.0.0.1;
    
    location /static/ {
        root /home/dmytro/Desktop/wks/linux_venv/my_1st_django/static_content;
    }

    location / {
        proxy_pass http://127.0.0.1:8081;
    }
	}

