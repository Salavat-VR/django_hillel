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
    email_to = models.EmailField("email_to")
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
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
