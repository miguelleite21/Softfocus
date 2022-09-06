
from django.shortcuts import get_object_or_404
from rest_framework import serializers,status
from events.serializers import EventsSerializer
from events.models import Events
from loss_communication.models import Loss_communication

class Loss_communicationSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    email = serializers.CharField(max_length=50)
    cpf = serializers.CharField(max_length=11)
    localization = serializers.CharField(max_length=100)
    type = serializers.CharField(max_length=20)
    date = serializers.DateField()
    event = serializers.CharField(max_length=20, write_only= True)
    events = EventsSerializer(read_only=True)

    def create(self, validated_data):
            event = validated_data.pop("event")
            events=  get_object_or_404(Events,name = event)
            communication = Loss_communication.objects.create(**validated_data,events = events)
            return communication

    def update(self, instance, validated_data):
        non_updatable = {"name", "cpf","localization","date","event","events"}
        
        for key, value in validated_data.items():
            if key in non_updatable:
                raise KeyError(
                    {"details": f"You con 't update the `{key}` key."},
                    status.HTTP_400_BAD_REQUEST,
                )

            setattr(instance, key, value)
            instance.save()

        return instance