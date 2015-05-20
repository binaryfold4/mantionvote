# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dynamicvote', '0003_auto_20150520_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='track',
            field=models.ForeignKey(related_name='track', to='dynamicvote.Track'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='voteset_current',
            field=models.BooleanField(default=1),
        ),
    ]
