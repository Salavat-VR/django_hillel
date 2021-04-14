from django.contrib import admin

from .models import Author, Post, Subscriber, Comment

admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Subscriber)
admin.site.register(Comment)
