from django.conf.urls import include, url
from django.contrib import admin
from dynamicvote.models import Track
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class TrackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Track
        resource_name = 'tracks'
        #fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'tracks', TrackViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

