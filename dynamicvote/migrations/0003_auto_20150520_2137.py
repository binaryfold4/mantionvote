# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dynamicvote', '0002_auto_20150520_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='sc_id',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]
