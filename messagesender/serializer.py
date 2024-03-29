from rest_framework import serializers
from api.models import User


class SendMessageSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=255)

    class Meta:
        model = User
