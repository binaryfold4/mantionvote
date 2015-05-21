from django.shortcuts import render
from dynamicvote.models import Track, Vote
from rest_framework import generics, permissions
from dynamicvote.serializers import TrackSerializer, VoteSerializer

class TrackView(generics.ListAPIView):
    model = Track
    permission_classes = (permissions.AllowAny,)
    serializer_class = TrackSerializer
    def get_queryset(self):
        return Track.objects.all()

class VoteView(generics.ListAPIView):
    model = Vote
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = VoteSerializer
    def get_queryset(self):
        user = self.request.user
        return Vote.objects.filter(voteset_current=1).filter(user=user)

def index(request):
    return render(request, 'index.html')


