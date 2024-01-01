from django.urls import path
from .views import (
    tech_api_view,
    project_api_view, 
    project_list_api_view,
    studies_latest_api_view,
    articles_latest_api_view,
)


urlpatterns = [
    path('techs/', tech_api_view, name='techs'),
    path('projects/', project_list_api_view, name='projects'),
    path('projects/<uuid:pk>', project_api_view, name='project-detail'),
    path('studies/latest/', studies_latest_api_view, name='studies-latest'),
    path('articles/latest/', articles_latest_api_view, name='articles-latest'),
]
