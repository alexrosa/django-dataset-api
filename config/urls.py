"""dataset-api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from rest_framework_swagger.views import get_swagger_view

from api_service.views import (EventTypeDetailView, EventTypeClearView, ActorView, EventTypeActorView, ActorStreakView)

schema_view = get_swagger_view(title='Dataset API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='docs/')),
    path('docs/', schema_view),
    path('erase/', EventTypeClearView.as_view(), name='event-erase'),
    path('events/', EventTypeDetailView.as_view(), name='event-detail'),
    path('events/actors/<int:actor_id>', EventTypeActorView.as_view(), name='event-actor'),
    path('actors/', ActorView.as_view(), name='actor-list'),
    path('actors/streak', ActorStreakView.as_view(), name='actor-streak-list'),
]
