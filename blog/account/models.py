import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField('email address', blank=False)
    confirmation_token = models.UUIDField(default=uuid.uuid4)


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file_path = models.ImageField(upload_to='blog/media_content')
