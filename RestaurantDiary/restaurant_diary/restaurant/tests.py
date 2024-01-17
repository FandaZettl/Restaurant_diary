from django.test import TestCase
from .models import Restaurant


class RestaurantModelTest(TestCase):
    def test_str_representation(self):
        restaurant = Restaurant(name='Test Restaurant', place='Test Place', cuisine_type='Test Cuisine')
        self.assertEqual(str(restaurant), 'Test Restaurant')
