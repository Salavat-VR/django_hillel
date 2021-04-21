from django.db import models
from django.utils.timezone import now


class Author(models.Model):
    class Meta:
        verbose_name = 'author'
        verbose_name_plural = 'authors'

    name = models.CharField("author's first name", max_length=50)
    email = models.CharField("author's email", max_length=20)

    def __str__(self):
        return self.name


class Subscriber(models.Model):
    subs_name = models.CharField("subs name", max_length=50)
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    email_to = models.EmailField("email_to")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(default=now)

    def __str__(self):
        return self.email_to


class Post(models.Model):
    title = models.CharField('Title', max_length=50)
    description = models.CharField('Description', max_length=90)
    content = models.TextField('Article')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(default=now)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('Post', null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField('Name', max_length=80)
    body = models.TextField('Body')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)


class Logger(models.Model):
    created = models.CharField('created time', max_length=20)
    time_execution = models.CharField('created time', max_length=20)
    path = models.TextField('path')
    utm = models.CharField('utm', max_length=20)
    i_p = models.CharField('utm', max_length=20)


class Book(models.Model):
    title = models.CharField('Title', max_length=250)
    author = models.ForeignKey("Author", on_delete=models.CASCADE, related_name='books')
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name='categories')


class Category(models.Model):
    category_option = models.CharField('Option', max_length=250)

    def __str__(self):
        return self.category_option
