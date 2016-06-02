from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.twitch.views import TwitchOAuth2Adapter
from rest_auth.registration.views import SocialLoginView


class FacebookLoginView(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
    client_class = OAuth2Client
    callback_url = 'http://localhost:8000/auth/facebook/'


class TwitchLoginView(SocialLoginView):
    adapter_class = TwitchOAuth2Adapter
    client_class = OAuth2Client
    callback_url = 'http://localhost:8000/auth/twitch/'
