from django.contrib import admin

from .models import Author, Book, Category, Comment, Logger, Post, Subscriber

admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Subscriber)
admin.site.register(Comment)
admin.site.register(Logger)
admin.site.register(Book)
admin.site.register(Category)
