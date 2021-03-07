from django.contrib.auth import get_user_model
from django.test import TestCase


class UserSignUpTest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.sign_up(
            email="admin@user.com",
            first_name="Admin",
            last_name="N3",
            password="admin@123",
            role="Admin",
        )

    def test_sign_up(self):
        self.assertEqual(self.user.email, "admin@user.com")

    def test_sign_up_duplicate(self):
        User = get_user_model()
        with self.assertRaises(Exception):
            User.sign_up(
                email="admin@user.com",
                first_name="Admin",
                last_name="N3",
                password="admin@123",
                role="Admin",
            )
