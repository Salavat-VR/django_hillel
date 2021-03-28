from django.db import models

from django.utils.timezone import now


class User(models.Model):
    class Meta:
        db_table = 'tbl_user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    name = models.CharField('first name', max_length=50)
    email = models.CharField('email', max_length=20)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField('The title of your masterpiece', max_length=50)
    description = models.CharField('Description', max_length=90)
    content = models.TextField('Paste ors Write it here :) ')
    created = models.DateTimeField(auto_created=True)
    updated = models.DateTimeField(default=now)
