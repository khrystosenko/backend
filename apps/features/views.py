from rest_framework.views import APIView
from rest_framework.response import Response

from apps.features.models import Feature
from apps.features.serializers import FeatureSerializer


class FeaturesView(APIView):
    """
    Fetch features list
    """

    def get(self, request):
        features = Feature.objects.all().order_by('order')
        return Response(FeatureSerializer(features, many=True).data)

