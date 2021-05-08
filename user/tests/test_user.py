from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class CreateUserTest(TestCase):
    """Test that users are created successfully"""

    def setUp(self):
        self.email = "mytest@email.com"
        self.username = "MyName"
        self.password = "MyTestPassword"
        self.new_user = User.objects.create_user(
            email=self.email,
            username=self.username,
            password=self.password
        )

    def test_create_user(self):
        """Test normal user is created"""

        self.assertEqual(self.new_user.email, self.email)
        self.assertEqual(self.new_user.username, self.username)
        self.assertTrue(self.new_user.check_password(self.password))
        self.assertTrue(self.new_user.is_active)
        self.assertFalse(self.new_user.is_staff)

    def test_create_superuser(self):
        """Test create super user"""

        email = "admin@email.com"
        username = "MyName"
        password = "MyTestPassword"
        first_name = "John"
        last_name = "Doe"
        admin = User.objects.create_superuser(
            email=email,
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )

        self.assertTrue(admin.is_active)
        self.assertTrue(admin.is_staff)
        self.assertTrue(admin.is_superuser)

    def test_normalized_email(self):
        """Test that the email was normalized"""

        email = 'mymail@EMAIL.COM'
        user = User.objects.create_user(
            email=email,
            username='myusername',
            password='mypassword'
        )
        self.assertEqual(user.email, email.lower())

    def test_create_user_invalid_credentials(self):
        """Test user creation with invalid credentials"""
        email = None
        username = 'MyUserName'
        password = 'password'

        with self.assertRaises(ValueError):
            User.objects.create_user(
                email=email,
                username=username,
                password=password
            )
