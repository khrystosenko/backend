from django.conf.urls import url

from apps.test.views import TestView


urlpatterns = [
    url(r'^$', TestView.as_view()),
]
