from django.conf.urls import patterns, url

from twitfollowing import views

urlpatterns = patterns('',
    url(r'^$', views.followed_users_list, name='followed'),
    url(r'^(?P<screen_name>.+)$', views.twits_from_user, name='twits' )
)