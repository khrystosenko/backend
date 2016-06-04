import time

from django.conf import settings
from rest_framework import serializers

from apps.features.models import Feature, FeatureVote, BATTLE, FEATURE_TYPES


class FeatureSerializer(serializers.ModelSerializer):
    votes = serializers.SerializerMethodField()

    def get_votes(self, feature):
        time_votes = (int(time.time() - settings.VOTES_START_TIME) / 3600) * settings.VOTES_PER_HOUR
        real_votes = feature.featurevote_set.count()
        if real_votes == 0:
            return real_votes

        return real_votes + time_votes

    class Meta:
        model = Feature
        fields = ('id', 'type', 'title', 'description', 'image_url', 'votes')


class FeatureVoteSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(default='')

    def validate_feature(self, value):
        if value.type != BATTLE:
            msg = 'Feature pk: {} is not of `{}` type.'.format(value.pk, FEATURE_TYPES[BATTLE])
            raise serializers.ValidationError(msg)

        return value

    class Meta:
        model = FeatureVote


class FeatureVoteUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureVote
        read_only_fields = ('id', 'feature')