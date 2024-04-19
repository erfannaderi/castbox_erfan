from rest_framework import viewsets
from rest_framework.response import Response
from .models import Playlist, Like, Comment
from .serialzier import PlaylistSerializer, LikeSerializer, CommentSerializer


class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

    def add_episode(self, request, pk=None):
        playlist = self.get_object()
        episode_id = request.data.get('episode_id')
        playlist.episodes.add(episode_id)
        return Response({'message': 'Episode added to playlist successfully.'})


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
