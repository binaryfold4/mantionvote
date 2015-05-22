from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.fields import CreationDateTimeField, ModificationDateTimeField

class Track(models.Model):
    sc_id = models.IntegerField(null=True, unique=True)
    uploaded_at = models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=2000, null=True)
    tag_list = models.CharField(max_length=200, null=True)
    duration = models.IntegerField(null=True)
    comment_count = models.IntegerField(null=True)
    download_count = models.IntegerField(null=True)
    playback_count = models.IntegerField(null=True)
    favoritings_count = models.IntegerField(null=True)
    stream_url = models.CharField(max_length=200, null=True)
    download_url = models.CharField(max_length=200, null=True)
    permalink_url = models.CharField(max_length=200, null=True)
    artwork_url = models.CharField(max_length=200, null=True)
    waveform_url = models.CharField(max_length=200, null=True)
    created_at = CreationDateTimeField()
    modified_at = ModificationDateTimeField()
    def __str__(self):
        return self.title

class Vote(models.Model):
    track = models.ForeignKey(Track, unique=False, related_name='track', null=False)
    user = models.ForeignKey(User, null=False)
    voteset_current = models.BooleanField(default=1)
    created_at = CreationDateTimeField()
    modified_at = ModificationDateTimeField()
    def __str__(self):
        return self.track.title




