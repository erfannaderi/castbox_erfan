import uuid

from django.db import models


class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Channel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    followers = models.ManyToManyField(User, through='useractivity.FollowedChannel', related_name='followed_channels')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
