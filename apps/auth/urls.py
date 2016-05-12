from django.conf.urls import url, include

from apps.auth.views import FacebookLoginView


urlpatterns = [
    url(r'^$', include('rest_auth.urls')),

    url(r'^facebook/$', FacebookLoginView.as_view(), name='fb_login'),
]
