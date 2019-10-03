from django.test import TestCase
from subby.models import User
import datetime, pytz

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(
            email = 'test@test.com',
            is_admin = False,
            password = 'password123',
            created_at = pytz.utc.localize(datetime.datetime.now()),
            updated_at = pytz.utc.localize(datetime.datetime.now())
        )

    def test_to_str(self):
        user = User.objects.get(email = 'test@test.com')
        self.assertEqual("{}".format(user), "test@test.com - admin: False")
