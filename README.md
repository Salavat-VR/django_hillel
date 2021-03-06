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


# Docker-related commands not to be forgotten

# show all
sudo docker container ls -a
sudo docker image ls -a
--------------------------------------------------
# remove image  -f: forced
sudo docker rmi -f _____(hash or name)

# remove container  -f: forced
sudo docker container rm _____(hash or name)
--------------------------------------------------
docker build -t ____(name)

also check in Makefile


sudo docker-compose build

sudo docker-compose up -d
or
sudo docker-compose up --build

sudo docker-compose down



# working with api 

implementing option_1

### views.py

	class PostSerializer(serializers.ModelSerializer):
		class Meta:
			model = Post
			fields = ("id", "title", "description", "content", "created", "updated")
	
	
	class PostAPIView(generics.RetrieveUpdateDestroyAPIView):
		queryset = Post.objects.all().order_by("id")
		serializer_class = PostSerializer

### main/urls.py

	path("api/v1/posts/", views.PostAPIView.as_view(), name='api_posts'),
    path("api/v1/posts/<int:pk>/", views.PostAPIView.as_view(), name='api_post')

