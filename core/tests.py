from django.test import TestCase
from core.models import Thing


class ThingTestCase(TestCase):
    def setUp(self):
        Thing.objects.create(name="lion", description="roar")
        Thing.objects.create(name="cat", description="meow")

    def test_things(self):
        """Animals that can speak are correctly identified"""
        thing = Thing.objects.get(name="lion")
        self.assertEqual(thing.description, 'roar')
