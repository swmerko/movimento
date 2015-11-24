# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('address', models.CharField(max_length=200, null=True, blank=True)),
                ('postcode', models.CharField(max_length=200, null=True, blank=True)),
                ('city', models.CharField(max_length=200, null=True, blank=True)),
                ('country', models.CharField(max_length=100, null=True, blank=True)),
                ('geo_lat', models.DecimalField(null=True, verbose_name=b'latitude', max_digits=13, decimal_places=10, blank=True)),
                ('geo_long', models.DecimalField(null=True, verbose_name=b'longitude', max_digits=13, decimal_places=10, blank=True)),
                ('title', models.CharField(max_length=256)),
                ('text', models.TextField(null=True, blank=True)),
                ('start_date', models.DateField(default=datetime.datetime.now)),
                ('end_date', models.DateField(null=True, blank=True)),
                ('reference_email', models.EmailField(max_length=254, null=True, blank=True)),
            ],
            options={
                'ordering': ['-start_date'],
            },
        ),
    ]
