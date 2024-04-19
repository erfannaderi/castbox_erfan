from django.contrib import admin
from .models import Comment, FollowedChannel, Like, Playlist


# Register your models here.

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(FollowedChannel)
class FollowerAdmin(admin.ModelAdmin):
    pass


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    pass
