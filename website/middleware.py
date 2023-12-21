# middleware.py
from django.http import HttpResponseRedirect
from django.conf import settings
from django.urls import reverse

class ComingSoonMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the "coming_soon" flag is set in settings
        if getattr(settings, 'COMING_SOON', False) and request.path != '/coming-soon':
            # Redirect all requests to the "coming soon" page
            path = reverse("website:coming_soon")
            return HttpResponseRedirect(path)

        response = self.get_response(request)
        return response
