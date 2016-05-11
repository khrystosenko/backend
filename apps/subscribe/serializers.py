from rest_framework import serializers


class SubscribeSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=128)
