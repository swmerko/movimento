from django.contrib import admin
from editorials.models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'reference_email')
    fields = (
        'title',
        'start_date',
        'end_date',
        'color',
        'reference_email',
        'reference_phone',
        'address',
        'postcode',
        'city',
        'country',
        'text',
        'geo_lat',
        'geo_long',
        'note'

    )
    readonly_fields = ('geo_lat', 'geo_long')


admin.site.register(Event, EventAdmin)
