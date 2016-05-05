from django.conf.urls import url

from apps.subscribe.views import MailChimpSubscribeView


urlpatterns = [
    url(r'^mailchimp/$', MailChimpSubscribeView.as_view()),
]
