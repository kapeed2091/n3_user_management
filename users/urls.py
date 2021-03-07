from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from users.views.user_profile_view import user_profile_view
from users.views.user_sign_up_view import user_sign_up

urlpatterns = [
    path("sign_up", user_sign_up),
    path("profile", user_profile_view),
]

urlpatterns = format_suffix_patterns(urlpatterns)
