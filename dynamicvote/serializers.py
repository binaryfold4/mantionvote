from dynamicvote.models import Track, Vote
from rest_framework import serializers

class TrackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Track

class TrackVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = [ 'sc_id', 'title' ]

class VoteSerializer(serializers.ModelSerializer):
    track = TrackVoteSerializer(read_only=True)
    class Meta:
        model = Vote
        #depth = 2
        fields = [ 'track' ] #, 'title' ]
