from django.conf.urls import patterns, include, url
from twitai import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^login-success$', views.loginSuccess),
    url(r'^login-error$', views.loginError),
    url(r'^secret$', views.secret),
)