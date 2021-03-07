from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from users.views.user_sign_up_view import user_sign_up

urlpatterns = [
    path("sign_up", user_sign_up),
]

urlpatterns = format_suffix_patterns(urlpatterns)
