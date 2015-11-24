from datetime import datetime

from core.models import TimeStampedModel, GeolocationModel
from django.db import models


class Event(TimeStampedModel, GeolocationModel):
    """
    Event model
    """
    title = models.CharField(max_length=256)
    text = models.TextField(blank=True, null=True)
    start_date = models.DateField(default=datetime.now)
    end_date = models.DateField(blank=True, null=True)
    reference_email = models.EmailField(blank=True, null=True)

    class Meta:
        ordering = ['-start_date']

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.update_coordinate(commit=False)
        super(Event, self).save(*args, **kwargs)
