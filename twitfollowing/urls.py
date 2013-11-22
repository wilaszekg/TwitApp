from django.conf.urls import patterns, url

from twitfollowing import views

urlpatterns = patterns('',
    url(r'^recommended$', views.recommended_users_list, name='recommended'),
    url(r'^followed$', views.followed_users_list, name='followed'),
    url(r'^twits/(?P<screen_name>.+)$', views.twits_from_user, name='twits' ),
    url(r'^search/(?P<screen_pattern>.+)$', views.find_screen, name='search' )
)