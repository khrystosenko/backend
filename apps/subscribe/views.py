from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response

from apps.subscribe.serializers import SubscribeSerializer
from libs.subscribe.mailchimp import validate_and_send_email


class MailChimpSubscribeView(APIView):
    """
    Subscribe to MailChimp list.
    """

    def post(self, request):
        data = SubscribeSerializer(data=request.data)
        data.is_valid(raise_exception=True)

        validate_and_send_email(data['email'].value, settings.MAILCHIMP_ROOMIT_LIST_ID)

        return Response()

