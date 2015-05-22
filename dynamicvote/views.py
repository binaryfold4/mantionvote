from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from dynamicvote.models import Track, Vote
from dynamicvote.serializers import TrackSerializer, VoteSerializer
from rest_framework import generics, permissions

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
    if request.POST:
        # move out of views.py

        oldv = Vote.objects.filter(user = request.user)
        oldv.update(voteset_current = 0)  # FIX: lazy, should only be changed after below is successful

        try:
            for voteno in range(1, 21):
                voteparam = "vote" + str(voteno)
                v = Vote()
                tc = Track.objects.get(sc_id=request.POST[voteparam])

                if Vote.objects.filter(track=tc, user=request.user, voteset_current=1):
                    raise ValueError("error: adding duplicate vote")

                v.track = tc
                v.user = request.user
                v.voteset_current = 1
                v.save()
        except:
            pass # FIX

        # iterate through voteX
        # ensure vote1-vote5 all exist
        # ensure each vote is unique
        # ensure each track ID is actually valid
        # set all votes of current user to current=0
        # add in each of these votes with current=1
        # respond with success message (which should be displayed on frontend)
        # otherwise respond with error

        return JsonResponse("saved", safe=False)

    else:
        return render(request, 'myvote.html')

def showvotes(request):
    return render(request, 'showvotes.html')

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
