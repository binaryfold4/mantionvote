from django.conf.urls import include, url
from django.contrib import admin
from dynamicvote import views

urlpatterns = [
    url(r'^$', views.index),

    url(r'^about/', views.about, name='about'),
    url(r'^myvote/', views.myvote, name='myvote'),
    url(r'^showvotes/all', views.showvotes, name='showvotes'),
    url(r'^profile/', views.updateprofile, name='profile'),

    url(r'^api/vote/', views.VoteView.as_view()),
    url(r'^api/tracks/', views.TrackView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

