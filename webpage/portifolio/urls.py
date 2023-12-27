from django.urls import path
from .views import IndexAPIView

urlpatterns = [
    path('', IndexAPIView.as_view(), name='index')
]
