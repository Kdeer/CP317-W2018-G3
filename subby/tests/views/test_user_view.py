from django.contrib.auth.decorators import login_required
from django.test import TestCase, Client
from django.urls import reverse
from subby.models import User
import datetime, pytz

class UserViewTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(
            email = 'test@test.com',
            is_admin = False,
            created_at = pytz.utc.localize(datetime.datetime.now()),
            updated_at = pytz.utc.localize(datetime.datetime.now())
        )
        user.set_password('password123')
        user.save()

        admin = User.objects.create(
            email = 'admin@test.com',
            is_admin = True,
            created_at = pytz.utc.localize(datetime.datetime.now()),
            updated_at = pytz.utc.localize(datetime.datetime.now())
        )
        admin.set_password('password123')
        admin.save()

        self.client.login(email='admin@test.com', password='password123')

    def test_index(self):
        expected_user = User.objects.get(email='test@test.com')
        response = self.client.get(reverse('subby:user_index'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['users'].count(), 1)
        self.assertEqual(response.context['users'].first().id, expected_user.id)

    def test_show(self):
        expected_user = User.objects.get(email='test@test.com')
        response = self.client.get(reverse('subby:user_show', kwargs={'user_id': expected_user.id}))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['user'], expected_user)

    def test_lock_account(self):
        locked_user = User.objects.get(email='test@test.com')
        self.assertEqual(locked_user.is_active, True)

        response = self.client.post(reverse('subby:user_lock_account', kwargs={'user_id': locked_user.id}))

        locked_user.refresh_from_db()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(locked_user.is_active, False)
