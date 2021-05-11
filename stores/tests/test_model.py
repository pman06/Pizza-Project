from django.test import TestCase
from stores.models import Pizzeria


# Create your tests here.
class CreateStoresTest(TestCase):
    """Test that stores are created successfully"""

    def test_store_str(self):
        """Test store is created successfully"""
        pizzeria_name = "Bobs Corner"
        street = "890, Sandy spring road"
        city = 'laurel'
        phone_number = "1453564309"
        shop = Pizzeria.objects.create(
            pizzeria_name=pizzeria_name,
            phone_number=phone_number,
            street=street,
            city=city
        )

        name_str = pizzeria_name + ", " + city
        self.assertEqual(str(shop), name_str)
