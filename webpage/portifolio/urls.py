from django.urls import path
from .views import studies_latest_api_view


urlpatterns = [
    path('studies/latest/', studies_latest_api_view, name='studies-latest'),
]
