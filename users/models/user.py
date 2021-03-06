from django.contrib.auth.models import AbstractUser
from django.db import models

from .abstract_datetime import AbstractDatetime


class User(AbstractUser, AbstractDatetime):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=32)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=32)
    state = models.CharField(max_length=32)
    zipcode = models.CharField(max_length=32)
    image = models.URLField()
    verified = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
