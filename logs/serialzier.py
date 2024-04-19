from rest_framework import serializers

from logs.models import Log, ViewedContent, ViewedChannel


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = '__all__'


class ViewedContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewedContent
        fields = '__all__'


class ViewedChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewedChannel
        fields = '__all__'
