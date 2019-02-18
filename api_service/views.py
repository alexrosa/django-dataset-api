from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response

from rest_framework.generics import GenericAPIView

from api_service.serializers import EventTypeSerializer, ActorSerializer
from api_service.services import EventTypeService, ActorEventService

#based_class
class BasedEventType(GenericAPIView):
    serializer_class = EventTypeSerializer

    def __init__(self):
        self.service = EventTypeService()


class EventTypeClearView(BasedEventType):

    def delete(self, request):
        self.service.erase_events()
        return Response(status=status.HTTP_200_OK)


class EventTypeDetailView(BasedEventType):

    def post(self, request):
        serializer = self.serializer_class(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        events = self.service.list_all()
        serializer = self.serializer_class(events, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class EventTypeActorView(BasedEventType):

    def get(self, request, actor_id):
        events = self.service.get_event_by_actor(actor_id=actor_id)
        serializer = self.serializer_class(events, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

#based_class
class BasedActorView(GenericAPIView):
    serializer_class = ActorSerializer

    def __init__(self):
        self.service = ActorEventService()


class ActorView(BasedActorView):

    def put(self, request):
        actor_id = request.data['id']
        actor = self.service.retrieve(actor_id=actor_id)
        _serializer = self.serializer_class(actor, data=request.data)
        if _serializer.is_valid():
            _serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        actors = self.service.get_all_actors()
        _serializer = self.serializer_class(actors, many=True)
        return Response(_serializer.data, status=status.HTTP_200_OK)


class ActorStreakView(BasedActorView):

    def get(self, request):
        actors = self.service.get_streaked_actors_list()
        _serializer = self.serializer_class(actors, many=True)
        return Response(_serializer.data, status=status.HTTP_200_OK)

