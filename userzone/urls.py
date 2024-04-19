from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserProfileViewSet, UserViewSet, ChannelViewSet

urlpatterns = [
    path('users/register/', UserRegistrationView.as_view()),
    path('users/login/', UserLoginView.as_view()),
    path('users/profile/', UserProfileViewSet.as_view({'get': 'list', 'put': 'update'})),
    path('users/<int:pk>/follow_channel/', UserViewSet.as_view({'post': 'follow_channel'})),
    path('users/<int:pk>/unfollow_channel/', UserViewSet.as_view({'post': 'unfollow_channel'})),
    path('users/<int:pk>/followed_channels/', UserViewSet.as_view({'get': 'followed_channels'})),
    path('channels/', ChannelViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('channels/<int:pk>/', ChannelViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]