from django.contrib import admin

from users.models import Permission


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "active"]
