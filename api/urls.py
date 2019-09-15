from rest_framework import routers
from api import views
from django.conf.urls import url, include

router = routers.DefaultRouter()
router.register(r'things', views.ThingViewSet, basename='thing')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]