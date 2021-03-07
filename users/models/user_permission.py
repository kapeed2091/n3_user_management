from django.db import models

from .abstract_datetime import AbstractDatetime


class UserPermission(AbstractDatetime):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    permission = models.ForeignKey("users.Permission", on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user_id", "permission_id")

    @classmethod
    def get_or_create(cls, user_id, permission_id):
        cls.objects.get_or_create(user_id=user_id, permission_id=permission_id)
