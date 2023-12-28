from django.urls import path
from .views import ProjectAPIView, profile_view

urlpatterns = [
    path('', profile_view, name='profile'),
    path('projects/', ProjectAPIView.as_view(), name='projects')
]
