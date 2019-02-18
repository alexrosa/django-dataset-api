from rest_framework import serializers

from api_service.models import EventType
from api_service.models import Actor
from api_service.models import Repository


class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = '__all__'


class RepositorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Repository
        fields = '__all__'


class EventTypeSerializer(serializers.ModelSerializer):
    actor = ActorSerializer(many=False, read_only=False)
    repository = RepositorySerializer(many=False, read_only=False)

    class Meta:
        model = EventType
        fields = '__all__'


