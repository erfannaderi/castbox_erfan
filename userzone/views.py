from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User, Channel
from .serialzier import UserSerializer, ChannelSerializer


class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully.'})
        return Response(serializer.errors, status=400)


class UserLoginView(APIView):
    def post(self, request):
        # Your login implementation
        return Response({'message': 'User logged in successfully.'})


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def follow_channel(self, request, pk=None):
        user = self.get_object()
        channel_id = request.data.get('channel_id')
        user.followed_channels.add(channel_id)
        return Response({'message': 'Channel followed successfully.'})

    def unfollow_channel(self, request, pk=None):
        user = self.get_object()
        channel_id = request.data.get('channel_id')
        user.followed_channels.remove(channel_id)
        return Response({'message': 'Channel unfollowed successfully.'})

    def followed_channels(self, request, pk=None):
        user = self.get_object()
        channels = user.followed_channels.all()
        serializer = ChannelSerializer(channels, many=True)
        return Response(serializer.data)


class ChannelViewSet(viewsets.ModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
