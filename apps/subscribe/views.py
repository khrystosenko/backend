from rest_framework.views import APIView
from rest_framework.response import Response

from apps.subscribe.serializers import SubscribeSerializer
from libs.subscribe import mailchimp


class MailChimpSubscribeView(APIView):
    """
    Subscribe to MailChimp list.
    """

    def post(self, request):
        data = SubscribeSerializer(data=request.data)
        data.is_valid(raise_exception=True)

        mailchimp.validate_and_send_email(data['email'].value)

        return Response()

