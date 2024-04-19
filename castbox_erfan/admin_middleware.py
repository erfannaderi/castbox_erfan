from django.http import HttpResponseForbidden


class RestrictAdminMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/my-custom-admin-url/'):
            if not request.user.is_staff:
                return HttpResponseForbidden("You are not authorized to access the admin interface.")
        response = self.get_response(request)
        return response
