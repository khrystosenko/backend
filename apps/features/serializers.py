from rest_framework import serializers
from apps.features.models import Feature


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ('type', 'title', 'description', 'image_url')

