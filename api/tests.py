from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from core.models import Thing


class ThingTests(APITestCase):
    def test_read_thing(self):
        url = reverse('thing-list')

        response = self.client.get(url, format='json', **{'HTTP_X_COMPANY':'kaleido'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_thing(self):
        """
        Ensure we can create a new thing object.
        """
        url = reverse('thing-list')

        data = {
            'name': 'TEST THING',
            'description': 'DESC'
        }
        headers = {
            'X-Company': 'kaleido'
        }
        response = self.client.post(url, data, format='json', headers=headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Thing.objects.count(), 1)
        self.assertEqual(Thing.objects.get().name, 'TEST THING')
