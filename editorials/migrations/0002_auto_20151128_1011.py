# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('editorials', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='color',
            field=models.CharField(blank=True, max_length=24, null=True, choices=[(b'red', 'Red'), (b'orange', 'Orange'), (b'yellow', 'Yellow'), (b'green', 'Green'), (b'blue', 'Blue'), (b'indigo', 'Indigo'), (b'violet', 'Violet')]),
        ),
        migrations.AddField(
            model_name='event',
            name='note',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateTimeField(help_text='Violet', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
