# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dynamicvote', '0005_auto_20150520_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='created_at',
            field=django_extensions.db.fields.CreationDateTimeField(blank=True, editable=False, default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='track',
            name='modified_at',
            field=django_extensions.db.fields.ModificationDateTimeField(blank=True, editable=False, default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='vote',
            name='created_at',
            field=django_extensions.db.fields.CreationDateTimeField(blank=True, editable=False, default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='vote',
            name='modified_at',
            field=django_extensions.db.fields.ModificationDateTimeField(blank=True, editable=False, default=django.utils.timezone.now),
        ),
    ]
