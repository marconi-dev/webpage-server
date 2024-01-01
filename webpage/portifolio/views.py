from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Study
from .serializers.serializers import LatestStudySerializer

@api_view(['GET'])
def studies_latest_api_view(request):
    """Lists latest studies"""
    studies = Study.objects.all()[:3]
    serializer = LatestStudySerializer(studies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
