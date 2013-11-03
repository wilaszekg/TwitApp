from django.conf.urls import patterns, include, url
from twitai import views, staff

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^login-error$', views.login_error),
    url(r'^staff$', staff.staff_main, name='staff'),
    url(r'^main$', views.main, name='main'),
    url(r'^logout$', views.logout, name='logout')
)