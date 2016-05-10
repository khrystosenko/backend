from django.conf.urls import url

from apps.features.views import FeaturesView


urlpatterns = [
    url(r'^$', FeaturesView.as_view()),
]
