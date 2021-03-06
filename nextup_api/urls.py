from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('media', views.MediaViewSet)
router.register('user', views.UserViewSet)
router.register('room', views.RoomViewSet)
router.register('response', views.ResponseViewSet)
router.register('review', views.ReviewViewSet)
router.register('blacklist', views.BlacklistViewSet)
router.register('join', views.RoomMemberViewSet)
router.register('results', views.ResultsViewSet, basename='results')

urlpatterns = [
    path('', include(router.urls)),
    path('blacklist/', views.blacklist),
    path('join/', views.join),
    path('media/', views.media),
    path('response/', views.response),
    path('review/', views.review),
    path('room/', views.room),
    path('user/', views.user),
    path('results/', views.results),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
