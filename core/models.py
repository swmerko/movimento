from core.utils import get_geo
from django.db import models


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class PublishedModel(models.Model):
    published = models.BooleanField(default=True)

    class Meta:
        abstract = True


class GeolocationModel(models.Model):
    address = models.CharField(max_length=200, blank=True, null=True)
    postcode = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    geo_lat = models.DecimalField('latitude', max_digits=13, decimal_places=10, blank=True, null=True)
    geo_long = models.DecimalField('longitude', max_digits=13, decimal_places=10, blank=True, null=True)

    class Meta:
        abstract = True

    def update_coordinate(self, commit=True):
        latitude, longitude = get_geo("%s, %s, %s, %s" % (self.address, self.postcode, self.city, self.country))
        if latitude and longitude:
            self.geo_lat = latitude
            self.geo_long = longitude
            if commit:
                self.save()

    def place_address(self):
        return "%s - %s %s, %s" % (self.address, self.postcode, self.city, self.country)
