from django.urls import path
from .views import (
    tech_api_view,
    ProjectAPIView,
    project_api_view, 
    profile_api_view,
)


urlpatterns = [
    path('', profile_api_view, name='profile'),
    path('techs/', tech_api_view, name='techs'),
    path('projects/', ProjectAPIView.as_view(), name='projects'),
    path('projects/<uuid:pk>', project_api_view, name='project-detail'),
]
