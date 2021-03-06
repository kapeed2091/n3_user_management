from django.db import models

from .abstract_datetime import AbstractDatetime
from .permission import Permission
from .user import User


class UserPermission(AbstractDatetime):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
