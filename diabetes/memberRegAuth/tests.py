from django.test import TestCase
from .models import regUser


class RegTest(TestCase):
    def set_up(self):
        newUser = regUser.objects.create(User__username='Test')

    def test_user(self):
        user = regUser.objects.all()
        print(user)

