# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dynamicvote', '0006_auto_20150520_2158'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='artwork_url',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='track',
            name='waveform_url',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
