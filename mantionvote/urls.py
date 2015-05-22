from django.conf.urls import include, url
from django.contrib import admin
from dynamicvote import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^api/vote/$', views.VoteView.as_view()),
    url(r'^api/tracks', views.TrackView.as_view()),
    url(r'^vote/$', views.dovote),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

