# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editorials', '0002_auto_20151128_1011'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='reference_phone',
            field=models.CharField(max_length=36, null=True, blank=True),
        ),
    ]
