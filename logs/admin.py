from django.contrib import admin

from logs.models import Log, ViewedChannel, ViewedContent


# Register your models here.
@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    pass


@admin.register(ViewedChannel)
class ViewedChannelAdmin(admin.ModelAdmin):
    pass


@admin.register(ViewedContent)
class ViewedContentAdmin(admin.ModelAdmin):
    pass
