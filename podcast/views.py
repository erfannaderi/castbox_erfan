from rest_framework import viewsets
from rest_framework.response import Response
from .models import Episode
from .serialzier import EpisodeSerializer


class EpisodeViewSet(viewsets.ModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer

    def mention(self, request, pk=None):
        episode = self.get_object()
        mentioned_users = request.data.get('mentioned_users', [])
        episode.mentioned_users.set(mentioned_users)
        return Response({'message': 'Users mentioned successfully.'})