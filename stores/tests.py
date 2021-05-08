from django.test import TestCase
from .models import Pizzeria


# Create your tests here.
class CreateStoresTest(TestCase):
    """Test that stores are created successfully"""

    def test_store_str(self):
        """Test store is created successfully"""
        pizzeria_name = "Bobs Corner"
        shop = Pizzeria.objects.create(pizzeria_name=pizzeria_name)

        self.assertEqual(str(shop), pizzeria_name)
