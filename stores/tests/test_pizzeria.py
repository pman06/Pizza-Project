from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from stores.models import Pizzeria
from stores.serializers import (PizzeriaListSerializer,
                                PizzeriaDetailSerializer,
                                )

CREATE_URL = reverse('pizzeria:pizzeria_create')


def detail_url(pizzeria_id):
    """Return details url for a pizzeria"""
    return reverse('pizzeria:pizzeria_detail', args=[pizzeria_id])


def update_url(pizzeria_id):
    """Return update url for a pizzeria"""
    return reverse('pizzeria:pizzeria_update', args=[pizzeria_id])


def sample_pizzeria(**params):
    """Create sample pizzeria for test purposes"""
    defaults = {
        'pizzeria_name': 'Sample Pizzeria',
    }
    defaults.update(params)
    return Pizzeria.objects.create(**defaults)


class PublicStoreAPITest(TestCase):
    """Test all public api for pizzeria"""

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_pizzeria_list_view(self):
        """Test that a pizzeria list is returned"""
        sample_pizzeria(pizzeria_name="DoDo Pizza")
        sample_pizzeria(pizzeria_name="Pauls plaze")

        url = reverse('pizzeria:pizzeria_list')
        res = self.client.get(url)

        pizzeria = Pizzeria.objects.all()
        serializer = PizzeriaListSerializer(pizzeria, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_retrieve_pizzeria_details_view(self):
        """Test that a pizzeria detail is returned"""
        pizzeria = sample_pizzeria(pizzeria_name="DoDo Pizza")
        url = detail_url(pizzeria.id)
        res = self.client.get(url)

        serializer = PizzeriaDetailSerializer(pizzeria)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(
            res.data['pizzeria_name'], serializer.data['pizzeria_name']
        )

    def test_create_pizzeria_view(self):
        """Test create new pizzeria view"""

        payload = {
            'pizzeria_name': "Dodo Pizza",
            'street': '8, Donny Lane',
            'city': 'Laurel',
            'state': 'MD',
            'zip_code': '20707',
            'website': 'https://www.dodopizzaplace.com',
            'description': 'Dodo place is your one stop shop for pizza',
            'email': 'admin@dodopizzaplace.com'
        }
        res = self.client.post(CREATE_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_credentials(self):
        """Test creating pizzeria with invalid credentials"""
        payload = {
            'pizzeria_name': '',
            'street': 'main street'
        }

        res = self.client.post(CREATE_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_full_update_pizzeria_view(self):
        """Test full pizzeria update view"""
        pizzeria = sample_pizzeria(pizzeria_name="My dodo pizza")
        payload = {
            'pizzeria_name': 'A new pizzeria',
            'street': 'Sample street',
            'city': 'Sample city',
            'state': 'Sample state',
            'zip_code': '23029',
            'website': 'http://www.mysite.com',
            'phone': '1938273849',
            'description': 'Your best pizza place',
            'email': 'myemail@gmail.com',
            'active': 'True'
        }

        url = update_url(pizzeria.id)
        res = self.client.put(url, payload)

        pizzeria.refresh_from_db()

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(pizzeria.street, payload['street'])
        self.assertEqual(pizzeria.city, payload['city'])
        self.assertEqual(pizzeria.zip_code, int(payload['zip_code']))
        self.assertEqual(pizzeria.description, payload['description'])

    def test_partial_update_pizzeria_view(self):
        """"Test partial update of the pizzeria"""
        pizzeria = sample_pizzeria()

        payload = {
            'pizzeria_name': 'New Update Name',
            'street': 'Lalubu street',
        }
        url = update_url(pizzeria.id)
        self.client.patch(url, payload)

        pizzeria.refresh_from_db()

        self.assertEqual(pizzeria.pizzeria_name, payload['pizzeria_name'])
        self.assertEqual(pizzeria.street, payload['street'])

    def test_pizzeria_delete_view(self):
        """Test Pizzeria Delete"""

        pizzeria = sample_pizzeria()
        url = reverse('pizzeria:pizzeria_delete', args=[pizzeria.id])

        res = self.client.delete(url)

        self.assertTrue(res.status_code, status.HTTP_204_NO_CONTENT)
