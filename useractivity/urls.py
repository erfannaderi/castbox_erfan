from django.urls import path
from .views import CommentViewSet, LikeViewSet, PlaylistViewSet

urlpatterns = [
    path('likes/', LikeViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('likes/<int:pk>/', LikeViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('comments/', CommentViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('comments/<int:pk>/', CommentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('playlists/', PlaylistViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('playlists/<int:pk>/', PlaylistViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('playlists/<int:pk>/add_episode/', PlaylistViewSet.as_view({'post': 'add_episode'})),
]