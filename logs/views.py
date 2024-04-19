from rest_framework import viewsets, permissions
from .models import ViewedContent, ViewedChannel, Log
from .serialzier import ViewedContentSerializer, ViewedChannelSerializer, LogSerializer


class ViewedContentViewSet(viewsets.ModelViewSet):
    serializer_class = ViewedContentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return ViewedContent.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ViewedChannelViewSet(viewsets.ModelViewSet):
    serializer_class = ViewedChannelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return ViewedChannel.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class LogViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = LogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Log.objects.filter(user=user)