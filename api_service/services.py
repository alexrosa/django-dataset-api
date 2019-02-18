from django.shortcuts import get_object_or_404, get_list_or_404
from django.db.models import Count, Max

from api_service.models import EventType, Actor


class EventTypeService:

    def retrieve(self, **kwargs):
        return get_object_or_404(EventType, **kwargs)

    def delete(self, id):
        obj = get_object_or_404(EventType, id=id)
        obj.delete()

    def erase_events(self):
        events = get_list_or_404(EventType)
        events.delete()

    def list_all(self):
        return EventType.objects.all().order_by('id')

    def get_event_by_actor(self, actor_id):
        return EventType.objects.filter(actor__id=actor_id)

class ActorEventService:

    def retrieve(self, **kwargs):
        return get_object_or_404(Actor, **kwargs)

    def get_all_actors(self):
        return Actor.objects.all().annotate(num_events=Count('event')).order_by('-num_events', '-created_at')

    def get_streaked_actors_list(self):
        return Actor.objects.all().annotate(num_days=Count('event__createad_at__day')).order_by('-created_at')
