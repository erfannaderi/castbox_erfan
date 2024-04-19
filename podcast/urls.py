from django.urls import path
from .views import EpisodeViewSet

urlpatterns = [
    path('episodes/', EpisodeViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('episodes/<int:pk>/', EpisodeViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('episodes/<int:pk>/mention/', EpisodeViewSet.as_view({'post': 'mention'})),
]