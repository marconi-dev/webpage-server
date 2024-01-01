from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Study
from .serializers import StudySerializer, LatestStudySerializer

# Create your views here.
class StudyViewSet(ReadOnlyModelViewSet):
    serializer_class = StudySerializer
    queryset = Study.objects.all()

    @action(['GET'], detail=False)
    def latest(self, request, *args, **kwargs):
        latest_queryset = self.get_queryset()[:3]
        serializer = LatestStudySerializer(latest_queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
