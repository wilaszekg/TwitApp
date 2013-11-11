from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from TwitApp import settings
from twitfollowing.models import FollowedUser
from twython import Twython
from social.apps.django_app.default.models import UserSocialAuth
from django.forms.models import modelform_factory

FollowedUserForm = modelform_factory(FollowedUser, fields=('twitter_screen_name',))


@login_required()
def followed_users_list(request):
    if request.method == 'POST':
        form = FollowedUserForm(request.POST)
        if form.is_valid():
            form.save()
            form = FollowedUserForm()
    else:
        form = FollowedUserForm()
    return render(request, 'twitfollowing/list.html', {'followed_users_list': FollowedUser.objects.all(),
                                                       'form' : form })

@login_required()
def twits_from_user(request, screen_name):
    tokens = UserSocialAuth.objects.get(user=request.user, provider='twitter').tokens
    twitter = Twython(settings.SOCIAL_AUTH_TWITTER_KEY,
                      settings.SOCIAL_AUTH_TWITTER_SECRET,
                      tokens['oauth_token'],
                      tokens['oauth_token_secret']
    )
    twits = twitter.get_user_timeline(screen_name=screen_name)

    return render(request, 'twitfollowing/twits.html', {'twits': twits, 'username': screen_name} )


