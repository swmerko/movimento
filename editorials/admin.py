from django.contrib import admin
from editorials.models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'reference_email')
    fields = (
        'title',
        'start_date',
        'end_date',
        'reference_email',
        'text',
        'address',
        'postcode',
        'city',
        'country',
        'geo_lat',
        'geo_long'
    )
    readonly_fields = ('geo_lat', 'geo_long')


admin.site.register(Event, EventAdmin)
