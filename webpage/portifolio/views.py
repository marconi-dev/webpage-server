from django.shortcuts import render
from .models import Profile


def about_me(request):
    TEMPLATE_NAME = "me.html"
    return render(request, TEMPLATE_NAME)


def index(request):
    TEMPLATE_NAME = "index.html"
    context = {
        "profile": Profile.objects.prefetch_related("links").first()
    }
    
    return render(request, TEMPLATE_NAME, context)
