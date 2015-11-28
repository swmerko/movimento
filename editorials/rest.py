from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializers import EventSerializer
from .models import Event


class EventViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing the accounts
    associated with the user.
    """
    permission_classes = (AllowAny, )
    serializer_class = EventSerializer
    queryset = Event.objects.all()
