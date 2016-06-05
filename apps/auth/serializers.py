from rest_auth.registration.serializers import SocialLoginSerializer


class DynamicCallbackURLSerializer(SocialLoginSerializer):
    def validate(self, attrs):
        request = self._get_request()
        view = self.context.get('view')
        view.callback_url = request.build_absolute_uri()

        return super(DynamicCallbackURLSerializer, self).validate(attrs)
