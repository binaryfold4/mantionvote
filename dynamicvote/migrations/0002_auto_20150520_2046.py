# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dynamicvote', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('voteset_current', models.NullBooleanField()),
                ('track', models.ForeignKey(to='dynamicvote.Track')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='voteset',
            name='track',
        ),
        migrations.RemoveField(
            model_name='voteset',
            name='user',
        ),
        migrations.DeleteModel(
            name='VoteSet',
        ),
    ]
