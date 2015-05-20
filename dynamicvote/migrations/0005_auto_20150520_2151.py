# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dynamicvote', '0004_auto_20150520_2139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='track',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='created_at',
        ),
    ]
