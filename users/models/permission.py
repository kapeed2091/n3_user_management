from django.db import models

from .abstract_datetime import AbstractDatetime


class Permission(AbstractDatetime):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
