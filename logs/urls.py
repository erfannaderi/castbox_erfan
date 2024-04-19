from django.urls import path, include
from rest_framework import routers
from .views import ViewedContentViewSet, ViewedChannelViewSet, LogViewSet

router = routers.DefaultRouter()
router.register('logs', LogViewSet)
router.register('viewed-content', ViewedContentViewSet)
router.register('viewed-channels', ViewedChannelViewSet)

urlpatterns = [
    # Other URL configurations
    path('api/', include(router.urls)),
]