from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.validators import UniqueValidator

from users.models import User


class UserSignUpRequestType:
    def __init__(self, email, first_name, last_name, password, role):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.role = role


class UserSignUpRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    role = serializers.CharField(required=True)

    def create(self, validated_data):
        user = User.sign_up(**validated_data)
        return UserSignUpRequestType(
            user.email,
            user.first_name,
            user.last_name,
            validated_data["password"],
            validated_data["role"],
        )


@api_view(["POST"])
def user_sign_up(request):
    serializer = UserSignUpRequestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
