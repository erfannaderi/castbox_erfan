from django.contrib import admin
from userzone.models import Channel, User


# Register your models here.
@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
