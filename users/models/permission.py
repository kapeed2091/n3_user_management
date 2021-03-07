from django.db import models

from .abstract_datetime import AbstractDatetime


class Permission(AbstractDatetime):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    active = models.BooleanField(default=True)

    @classmethod
    def get_or_create(cls, name, description=""):
        permission, is_created = cls.objects.get_or_create(name=name)
        if not is_created:
            permission.description = description
            permission.save()

        return permission
