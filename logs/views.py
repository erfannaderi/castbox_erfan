from celery.worker import request
from rest_framework import viewsets
from .models import ViewedContent, ViewedChannel, Log
from .serialzier import ViewedContentSerializer, ViewedChannelSerializer, LogSerializer



class ViewedContentViewSet(viewsets.ModelViewSet):
    queryset = ViewedContent.objects.all()
    serializer_class = ViewedContentSerializer


class ViewedChannelViewSet(viewsets.ModelViewSet):
    queryset = ViewedChannel.objects.all()
    serializer_class = ViewedChannelSerializer


class LogViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
