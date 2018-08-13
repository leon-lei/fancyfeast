from django.test import TestCase
from django.contrib.auth.models import User


from accounts.models import UserProfile
from tribes.models import Event, Tribe


class TribeModelTest(TestCase):

        @classmethod
        def setUpTestData(cls):
            #Set up non-modified objects used by all test methods
            # Create User
            u = User.objects.get_or_create(email='alpha@example.com', username='alpha35', first_name='Alpha', last_name='Omega')[0]
            u.set_password('something')
            u.save()

            # Create UserProfile
            alpha = UserProfile.objects.filter(user=User.objects.get(username='alpha35'))[0]

            # Create Tribe
            t = Tribe.objects.create(name='Breakfast', description='First meal of the day', chieftain=alpha)
            t.tribesmen.add(alpha)
            t.save()

        def test_get_absolute_url(self):
            tribe = Tribe.objects.get(id=1)
            #This will also fail if the urlconf is not defined.
            self.assertEquals(tribe.get_absolute_url(), '/tribes/1/')