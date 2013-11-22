"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.contrib.auth.models import User

from django.test import TestCase
from django.test import Client
from twitfollowing.models import FollowedUser
from mock import Mock
from twitfollowing.views import FollowedUsersStrategy


class FollowingTest(TestCase):
    fixtures = ['test_data.json']
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')

    def test_add_new_recommended_user(self):
        response = self.client.post('/twitter/recommended', {'twitter_screen_name': 'stefan'})
        self.assertEqual(response.status_code, 200)
        new_user = FollowedUser.objects.get(twitter_screen_name='stefan')
        self.assertEqual(new_user.twitter_screen_name, 'stefan')

    def test_recommended_users_list(self):
        response = self.client.get('/twitter/recommended')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['followed_users_list']), 5)

    def test_list_followed_users(self):
        twython_mock = Mock()
        factory_mock = Mock()
        factory_mock.return_value = twython_mock
        twython_mock.get_friends_ids.return_value = {"ids": [1, 2]}
        twython_mock.lookup_user.return_value = [{"screen_name": "a"}, {"screen_name": "b"}]
        strategy = FollowedUsersStrategy(factory_mock)
        user_names = strategy.all_users(Mock())
        self.assertEqual(user_names, [{'twitter_screen_name': 'a'}, {'twitter_screen_name': 'b'}])

    def test_add_followed_user(self):
        twython_mock = Mock()
        factory_mock = Mock()
        factory_mock.return_value = twython_mock
        strategy = FollowedUsersStrategy(factory_mock)
        strategy.save(Mock(), Mock())
        self.assertEqual(twython_mock.create_friendship.call_count, 1)
