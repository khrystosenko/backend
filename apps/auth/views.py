from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView


class FacebookLoginView(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
