from django.urls import path
from .views import profile_api_view


urlpatterns = [
    path('profile/', profile_api_view, name='projects'),
]
