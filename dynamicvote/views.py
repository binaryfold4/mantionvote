from django.shortcuts import render
from dynamicvote.models import Track, Vote
from rest_framework import viewsets
from dynamicvote.serializers import TrackSerializer, VoteSerializer

class TrackViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

class VoteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Vote.objects.filter(voteset_current=1) #.filter(user=request.user)
    serializer_class = VoteSerializer

def index(request):
    return render(request, 'dynamicvote/index.html')

