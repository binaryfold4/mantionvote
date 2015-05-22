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

def dovote(request):
    if request.method == 'POST':
        vote_text = request.POST.get('vote')

        print(request.POST)
        response_data = {}

        #post = Post(text=post_text, author=request.user)
        #post.save()

        response_data['result'] = 'Create post successful!'
        #response_data['postpk'] = post.pk
        #response_data['text'] = post.text
        #response_data['created'] = post.created.strftime('%B %d, %Y %I:%M %p')
        #response_data['author'] = post.author.username



        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"error": "there was a problem"}),
            content_type="application/json"
        )