from django.test import TestCase, Client
from django.urls import reverse

class UserViewTestCase(TestCase):
    def test_index(self):
      response = self.client.get(reverse('subby:index'))
      self.assertEqual(response.status_code, 200)
