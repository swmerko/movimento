from django.shortcuts import render
from .models import Event


def events_map(request):
    events = Event.objects.exclude(geo_lat__isnull=True, geo_long__isnull=True)

    context = {
        'events': events,
    }

    return render(request, 'editorials/map.html', context)
