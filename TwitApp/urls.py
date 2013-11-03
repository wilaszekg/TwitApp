from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from twitai import views
import twitai

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TwitApp.views.home', name='home'),
    # url(r'^TwitApp/', include('TwitApp.foo.urls')),
    url(r'^tai/', include('twitai.urls', namespace="twitai")),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Social Auth
    url('', include('social.apps.django_app.urls', namespace='social')),
)
