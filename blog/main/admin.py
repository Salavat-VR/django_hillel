from django.contrib import admin

from .models import Post, Author, Subscriber

admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Subscriber)
