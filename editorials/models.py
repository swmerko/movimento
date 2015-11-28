from datetime import datetime

from core.models import TimeStampedModel, GeolocationModel
from django.db import models
from django.utils.translation import ugettext as _

COLORS = (
    ('red', _('Red')),
    ('orange', _('Orange')),
    ('yellow', _('Yellow')),
    ('green', _('Green')),
    ('blue', _('Blue')),
    ('indigo', _('Indigo')),
    ('violet', _('Violet')),
)


class Event(TimeStampedModel, GeolocationModel):
    """
    Event model
    """
    title = models.CharField(max_length=256)
    text = models.TextField(blank=True, null=True)
    start_date = models.DateTimeField(default=datetime.now)
    end_date = models.DateTimeField(blank=True, null=True, help_text=_('Violet'))
    reference_email = models.EmailField(blank=True, null=True)
    color = models.CharField(max_length=24,
                             choices=COLORS,
                             blank=True,
                             null=True)
    note = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-start_date']

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.update_coordinate(commit=False)
        super(Event, self).save(*args, **kwargs)
