import json
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse

from django.shortcuts import render
from TwitApp import settings
from twitfollowing.models import FollowedUser
from twython import Twython
from twython import TwythonAuthError
from social.apps.django_app.default.models import UserSocialAuth
from django.forms.models import modelform_factory

FollowedUserForm = modelform_factory(FollowedUser, fields=('twitter_screen_name',))


def get_twython(request):
    tokens = UserSocialAuth.objects.get(user=request.user, provider='twitter').tokens
    twitter = Twython(settings.SOCIAL_AUTH_TWITTER_KEY,
                      settings.SOCIAL_AUTH_TWITTER_SECRET,
                      tokens['oauth_token'],
                      tokens['oauth_token_secret']
    )
    return twitter


class RecommendedUsersStrategy:
    type = "recommended"

    def __init__(self):
        pass

    def save(self, request, form):
        form.save()

    def all_users(self, request):
        return FollowedUser.objects.all()


class FollowedUsersStrategy:
    type = "followed"

    def __init__(self, twitter_factory):
        self.twitter_factory = twitter_factory

    def save(self, request, form):
        twitter = self.twitter_factory(request)
        twitter.create_friendship(screen_name=form.instance.twitter_screen_name)

    def all_users(self, request):
        twitter = self.twitter_factory(request)
        response = twitter.get_friends_ids(screen_name=request.user.username)
        ids = [str(id) for id in response["ids"]]
        users = twitter.lookup_user(user_id=", ".join(ids))
        names = [{"twitter_screen_name": u["screen_name"]} for u in users]
        return names


def users_list_factory(serving_strategy):
    @login_required()
    def view(request):
        if request.method == 'POST':
            form = FollowedUserForm(request.POST)
            if form.is_valid():
                serving_strategy.save(request, form)
                form = FollowedUserForm()
        else:
            form = FollowedUserForm()
        return render(request, 'twitfollowing/list.html', {'followed_users_list': serving_strategy.all_users(request),
                                                           'form': form, 'type': serving_strategy.type})

    return view


recommended_users_list = users_list_factory(RecommendedUsersStrategy())
followed_users_list = users_list_factory(FollowedUsersStrategy(get_twython))


@login_required()
def twits_from_user(request, screen_name):
    try:
        twitter = get_twython(request)
        twits = twitter.get_user_timeline(screen_name=screen_name)
    except TwythonAuthError:
        return render(request, 'error.html', {'message': 'This is private twitter profile'})

    return render(request, 'twitfollowing/twits.html', {'twits': twits, 'username': screen_name})


@login_required()
def find_screen(request, screen_pattern):
    twitter = get_twython(request)
    users = twitter.search_users(q=screen_pattern, count=10)
    return HttpResponse(json.dumps(users), content_type="application/json")

