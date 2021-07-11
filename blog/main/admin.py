from django.contrib import admin

from account.models import User, Avatar
from .models import Author, Post

admin.site.register(Author)
admin.site.register(Post)
# admin.site.register(Subscriber)
# admin.site.register(Comment)
# admin.site.register(Logger)
# admin.site.register(Book)
# admin.site.register(Category)
admin.site.register(User)
admin.site.register(Avatar)
