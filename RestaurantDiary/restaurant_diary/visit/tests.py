from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from restaurant.models import Restaurant
from .models import Visit


class VisitModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.restaurant = Restaurant.objects.create(name='Test Restaurant', place='Test Place',
                                                    cuisine_type='Test Cuisine')

    def test_str_representation(self):
        visit = Visit(user=self.user, restaurant=self.restaurant, date_visited='2024-01-01', expense=500.00,
                      note='Test Note', rating=4)
        self.assertEqual(str(visit), 'Test Restaurant - 2024-01-01')

    def test_user_assigned_on_create(self):
        visit = Visit.objects.create(restaurant=self.restaurant, date_visited='2024-01-01', expense=500.00,
                                     note='Test Note', rating=4)
        self.assertEqual(visit.user, self.user)


class VisitViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.restaurant = Restaurant.objects.create(name='Test Restaurant', place='Test Place',
                                                    cuisine_type='Test Cuisine')
        self.visit = Visit.objects.create(user=self.user, restaurant=self.restaurant, date_visited='2024-01-01',
                                          expense=500.00, note='Test Note', rating=4)

    def test_visit_list_view(self):
        url = reverse('visit-list-create')
        self.client.force_login(self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Restaurant')

    def test_visit_detail_view(self):
        url = reverse('visit-detail', args=[self.visit.id])
        self.client.force_login(self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Restaurant')
