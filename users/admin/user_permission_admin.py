from django.contrib import admin

from users.models import UserPermission


@admin.register(UserPermission)
class UserPermissionAdmin(admin.ModelAdmin):
    list_display = ["user_id", "permission_id"]
    raw_id_fields = ["user", "permission"]
