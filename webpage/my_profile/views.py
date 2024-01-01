from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Profile
from .serializers import ProfileSerializer


@api_view(['GET'])
def profile_api_view(request):
    profile = Profile.objects.prefetch_related('links').first()
    serializer = ProfileSerializer(profile)
    return Response(serializer.data, status=status.HTTP_200_OK)   
