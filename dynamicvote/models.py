from django.db import models
from django.contrib.auth.models import User

class Track(models.Model):
    sc_id = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
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

class VoteSet(models.Model):
    track = models.ForeignKey(Track)
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    voteset_current = models.NullBooleanField()

#currvote
#- track_id
#- total_vote
#- last_updated



