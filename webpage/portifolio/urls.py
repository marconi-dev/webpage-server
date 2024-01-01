from django.urls import path
from .views import (
    studies_latest_api_view,
    articles_latest_api_view,
)


urlpatterns = [
    path('studies/latest/', studies_latest_api_view, name='studies-latest'),
    path('articles/latest/', articles_latest_api_view, name='articles-latest'),
]
