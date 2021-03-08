from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from users.token import token_generator


@api_view(["GET"])
def verify_email(request, verify_token):
    is_valid, user = token_generator.check_token(verify_token)
    if is_valid:
        email = user.email
        User = get_user_model()
        try:
            user = User.objects.get(email=email)
            if user.verified:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                user.verified = True
                user.save()
                return Response(status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
