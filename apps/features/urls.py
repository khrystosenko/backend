from django.conf.urls import url

from apps.features.views import FeaturesView, FeaturesVoteView, FeaturesVoteUpdateView


urlpatterns = [
    url(r'^$', FeaturesView.as_view()),
    url(r'^vote/$', FeaturesVoteView.as_view()),
    url(r'^vote/(?P<vote_id>\d+)/$', FeaturesVoteUpdateView.as_view())
]
