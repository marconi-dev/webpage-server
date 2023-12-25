from django.urls import path
from .views import about_me, index

urlpatterns = [
    path('', index, name='index'),
    path('me/', about_me, name='about-me')
]
