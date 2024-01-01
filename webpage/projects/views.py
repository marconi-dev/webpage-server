from django.db.models import Count
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from .serializers.project import ProjectDetailSerializer, ProjectSerializer
from .serializers.technology import TechnologySerializer
from .models import Project, Technology

# Create your views here.

class ProjectViewSet(ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
    # TODO default retrieve was returning complete url for image fields
    def retrieve(self, request, *args, **kwargs):
        serializer = ProjectDetailSerializer(self.get_object())
        return Response(serializer.data, status=status.HTTP_200_OK)


class TechnologyViewSet(ReadOnlyModelViewSet):
    serializer_class = TechnologySerializer

    def get_queryset(self):
        return (
             Technology.objects
            .annotate(tech_count=Count('techs'))
            .filter(tech_count__gt=0, techs__is_equipe_tech=False)
            .order_by('-tech_count', 'name')
            .values('name', 'id', 'tech_count')
        )
