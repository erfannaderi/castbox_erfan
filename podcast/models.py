import uuid

from django.db import models
from django.utils.timezone import now


# Create your models here.
class Podcast(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()

    # image = models.ImageField(upload_to='')

    def __str__(self):
        return self.title


class Episode(models.Model):
    title = models.CharField(max_length=250)
    audio_file = models.FileField(upload_to='episodes/', null=True, blank=True)
    channel = models.ForeignKey('userzone.Channel', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    description = models.TextField()
    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
