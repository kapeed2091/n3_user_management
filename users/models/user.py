from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

from users.token import token_generator
from users.utils.send_email import send_email

from .abstract_datetime import AbstractDatetime
from .permission import Permission
from .user_permission import UserPermission


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser, AbstractDatetime):
    username = None
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=32)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=32)
    state = models.CharField(max_length=32)
    zipcode = models.CharField(max_length=32)
    image = models.URLField()
    verified = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    @classmethod
    def create(cls, email, first_name, last_name, password, role):
        user = cls.objects.create(
            email=email, first_name=first_name, last_name=last_name, password=password
        )
        # Assumption that password is sent in encrypted form as configured in default Django settings
        # https://docs.djangoproject.com/en/3.1/topics/auth/passwords/

        permission = Permission.get_or_create(name=role)
        UserPermission.get_or_create(user_id=user.id, permission_id=permission.id)

        cls.send_email(user)

        return user

    @classmethod
    def send_email(cls, user):
        # TODO: What should be text for subject and body
        subject = "Please verify your email"
        body = "Click on the link: {base_url}/api/users/verify/{token}".format(
            base_url=settings.BASE_URL, token=token_generator.make_token(user)
        )
        send_email(settings.EMAIL_SENDER, user.email, subject, body)

    @classmethod
    def sign_up(cls, email, first_name, last_name, password, role):
        try:
            cls.objects.get(email=email)
            raise Exception("User with email: {} already exists".format(email))
            # TODO: Move exception messages to common place
            # TODO: Strings should be in I18N compatible format
        except cls.DoesNotExist:
            user = cls.create(email, first_name, last_name, password, role)

        return user
