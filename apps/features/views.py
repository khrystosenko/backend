from django.conf import settings
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response

from apps.features.models import Feature, FeatureVote
from apps.features.serializers import FeatureSerializer, FeatureVoteSerializer, FeatureVoteUpdateSerializer
from apps.features.throttles import VoteAnonRateThrottle
from libs.subscribe.mailchimp import validate_and_send_email


class FeaturesView(APIView):

    def get(self, request):
        features = Feature.objects.all().order_by('order')
        return Response(FeatureSerializer(features, many=True).data)


class FeaturesVoteView(APIView):
    throttle_classes = (VoteAnonRateThrottle,) if not settings.TEST_SERVER else tuple()

    def send_email(self, instance):
        if instance.email:
            validate_and_send_email(instance.email, settings.MAILCHIMP_BATTLE_LIST_ID)

    def post(self, request):
        serialized = FeatureVoteSerializer(data=request.data)
        serialized.is_valid(raise_exception=True)
        instance = serialized.save()
        self.send_email(instance)

        return Response({'id': instance.pk})

    def put(self, request, vote_id):
        instance = get_object_or_404(FeatureVote, pk=vote_id)
        data = {'email': request.data.get('email')}
        serialized = FeatureVoteUpdateSerializer(instance, data=request.data, partial=True)
        serialized.is_valid(raise_exception=True)
        self.send_email(serialized.save(update_fields=['email']))

        return Response()