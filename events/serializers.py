from rest_framework import serializers


class EventsSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
