from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns

from users.views.user_profile_view import user_profile_view
from users.views.user_sign_up_view import user_sign_up
from users.views.verify_email_view import verify_email

urlpatterns = [
    path("sign_up", user_sign_up),
    path("profile", user_profile_view),
    re_path("^verify/(?P<verify_token>.+)/$", verify_email),
]

urlpatterns = format_suffix_patterns(urlpatterns)
