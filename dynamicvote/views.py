from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django import forms
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from rest_framework import generics, permissions
from dynamicvote.serializers import TrackSerializer, VoteSerializer
from dynamicvote.models import Track, Vote

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

class UserInfoForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('email',)

def index(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('myvote'))
    else:
        return render(request, 'index-notloggedin.html')

def about(request):
    return render(request, 'about.html')

@login_required
def myvote(request):
    return render(request, 'myvote.html')

def showvotes(request):
    return render(request, 'showvotes.html')

@login_required
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

@login_required
def updateprofile(request):
    if request.POST:
        user_form = UserInfoForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('myvote'))
    else:
        user_form = UserInfoForm()
    return render_to_response('profile.html', {'user_form': user_form}, context_instance=RequestContext(request))
