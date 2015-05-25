# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dynamicvote', '0007_auto_20150522_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='track',
            field=models.ForeignKey(to='dynamicvote.Track'),
        ),
    ]
