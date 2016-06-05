from django.conf import settings
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response

from apps.features.models import Feature, FeatureVote
from apps.features.serializers import FeatureSerializer, FeatureVoteSerializer, FeatureVoteUpdateSerializer
from apps.features.throttles import VoteAnonRateThrottle
from libs.subscribe.mailchimp import validate_and_send_email
from libs.decorators import APIThrottleWrapper


class FeaturesView(APIView):

    def get(self, request):
        features = Feature.objects.all().order_by('order')
        return Response(FeatureSerializer(features, many=True).data)


@APIThrottleWrapper([VoteAnonRateThrottle])
class FeaturesVoteView(APIView):
    def post(self, request):
        serialized = FeatureVoteSerializer(data=request.data)
        serialized.is_valid(raise_exception=True)
        instance = serialized.save()
        
        validate_and_send_email(instance.email, settings.MAILCHIMP_BATTLE_LIST_ID)

        return Response({'id': instance.pk})


@APIThrottleWrapper([VoteAnonRateThrottle])
class FeaturesVoteUpdateView(APIView):
    def put(self, request, vote_id):
        instance = get_object_or_404(FeatureVote, pk=vote_id)
        data = {'email': request.data.get('email')}
        serialized = FeatureVoteUpdateSerializer(instance, data=request.data, partial=True)
        serialized.is_valid(raise_exception=True)
        instance = serialized.save(update_fields=['email'])

        validate_and_send_email(instance.email, settings.MAILCHIMP_BATTLE_LIST_ID)

        return Response()
