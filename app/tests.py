from django.test import TestCase
from django.contrib.auth.models import User
from .models import *

# Create your tests here.
class TestUsersandPosts(TestCase):
    def setUp(self):
        self.users = [
            {
                "username": "JodaFTW",
                "password": "mama123*",
            },
            {
                "username": "lilflud",
                "password": "basecamp01",
            },
        ]

        for user in self.users:
            User.objects.create(
                username=user["username"],
                password=user["password"],
            )

        self.posts = [
            {
                "header": "LFM I need 4 more for a raid",
                "platform": "XBOX",
            },
        ]

    def test_create_user(self):
        assert len(User.objects.all()) == len(self.users)
        print(User.objects.get(username="JodaFTW"))
