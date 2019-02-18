from django.db import models

from django.utils.timezone import now
from config import settings

class Actor(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)
    login = models.TextField(blank=False, null=False)
    avatar_url = models.TextField(blank=True, null=True)


class Repository(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)
    name = models.TextField()
    url = models.TextField()


class EventType(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)
    type = models.TextField()
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, null=False)
    repo = models.ForeignKey(Repository, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)