from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):
    """Test all forms are available on the admin page"""

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="mymail@email.com",
            username='myusername',
            password="password123",
        )

        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email="testemaiil@email.com",
            username="myusername",
            password="passwordtest",
            first_name="John",
            last_name="Doe",
        )

    def test_users_created(self):
        """Test that users are listed on users page"""
        url = reverse('admin:user_myuser_changelist')
        response = self.client.get(url)
        self.assertTrue(get_user_model().objects.exists())

        self.assertContains(response, self.user.email)
        self.assertContains(response, self.user.username)
        self.assertContains(response, self.user.first_name)
        self.assertContains(response, self.user.last_name)

    def test_user_change(self):
        """Test the user edit page works"""
        url = reverse('admin:user_myuser_change', args=(self.user.id,))
        response = self.client.get(url)

        self.assertEquals(response.status_code, 200)
