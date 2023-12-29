from django.db.models import Count
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Profile, Project, Technology
from .serializers.serializers import (
    ProfileSerializer, 
    ProjectSerializer, 
    TechnologySerializer,
    ProjectDetailSerializer
)


@api_view(['GET'])
def project_list_api_view(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def profile_api_view(request):
    profile = Profile.objects.prefetch_related('links').first()
    serializer = ProfileSerializer(profile)
    return Response(serializer.data, status=status.HTTP_200_OK)   

@api_view(['GET'])
def tech_api_view(request):
    techs = (
        Technology.objects
        .annotate(tech_count=Count('techs'))
        .filter(tech_count__gt=0)
        .order_by('tech_count', 'name')
        .values('name', 'id', 'tech_count')
    )
    serializer = TechnologySerializer(techs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def project_api_view(request, pk):
    project = get_object_or_404(Project, pk=pk)
    serializer = ProjectDetailSerializer(project)
    return Response(serializer.data, status=status.HTTP_200_OK)
