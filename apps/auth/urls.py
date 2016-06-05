from django.conf.urls import url, include

from apps.auth.views import FacebookLoginView, TwitchLoginView


urlpatterns = [
    url(r'^', include('rest_auth.urls')),

    url(r'^facebook/$', FacebookLoginView.as_view(), name='fb_login'),
    url(r'^twitch/$', TwitchLoginView.as_view(), name='twitch_login'),
]
