import pytest
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db

class TestUserProfile:
    def test_model(self):
        obj = mixer.blend('accounts.UserProfile')
        assert obj.pk == 1, 'Should create a UserProfile instance'