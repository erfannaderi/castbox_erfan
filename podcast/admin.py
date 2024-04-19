from django.contrib import admin

from podcast.models import Podcast, Episode


# Register your models here.

# class EpisodeInline(admin.TabularInline):
#     model = Episode


@admin.register(Podcast)
class PodcastAdmin(admin.ModelAdmin):
    pass


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    pass
