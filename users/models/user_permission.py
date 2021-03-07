from django.db import models

from .abstract_datetime import AbstractDatetime


class UserPermission(AbstractDatetime):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    permission = models.ForeignKey("users.Permission", on_delete=models.CASCADE)
