class UserActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user

        if user.is_authenticated:
            viewed_episodes = request.GET.getlist('viewed_episodes')
            viewed_channels = request.GET.getlist('viewed_channels')
            viewed_podcasts = request.GET.getlist('viewed_podcasts')
            user.episodes_viewed.add(*viewed_episodes)
            user.channels_viewed.add(*viewed_channels)
            user.podcasts_viewed.add(*viewed_podcasts)

        response = self.get_response(request)
        return response
