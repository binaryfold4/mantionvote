# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('sc_id', models.IntegerField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('uploaded_at', models.CharField(max_length=200, null=True)),
                ('title', models.CharField(max_length=200, null=True)),
                ('description', models.CharField(max_length=2000, null=True)),
                ('tag_list', models.CharField(max_length=200, null=True)),
                ('duration', models.IntegerField(null=True)),
                ('comment_count', models.IntegerField(null=True)),
                ('download_count', models.IntegerField(null=True)),
                ('playback_count', models.IntegerField(null=True)),
                ('favoritings_count', models.IntegerField(null=True)),
                ('stream_url', models.CharField(max_length=200, null=True)),
                ('download_url', models.CharField(max_length=200, null=True)),
                ('permalink_url', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VoteSet',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('voteset_current', models.NullBooleanField()),
                ('track', models.ForeignKey(to='dynamicvote.Track')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
