from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Profile, Project, Technology
from .serializers.serializers import (
    ProfileSerializer, 
    ProjectSerializer, 
    TechnologySerializer,
    ProjectDetailSerializer
)


class ProjectAPIView(APIView):
    http_method_names = ('get',)

    def get_projects(self):
        projects = Project.objects.all()
        query_params = self.request.query_params

        project_type = query_params.get('project_type')
        if project_type in ['backend', 'fun', 'cs']:
            projects = projects.filter(project_type=project_type)

        technologies = query_params.getlist('technologies')
        if technologies:
            # WARNING slow query. Avoid server side filtering
            # against technologies
            query = Q()
            for tech in technologies:
                query |= Q(name__icontains=tech)

            techs = Technology.objects.filter(query).values_list('id')
            projects = projects.filter(tecnologies__in=techs).distinct('id')

        return projects

    def get(self, request, *args, **kwargs):
        projects = self.get_projects()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def profile_api_view(request):
    profile = Profile.objects.prefetch_related('links').first()
    serializer = ProfileSerializer(profile)
    return Response(serializer.data, status=status.HTTP_200_OK)   

@api_view(['GET'])
def tech_api_view(request):
    techs = Technology.objects.values('name', 'id')
    serializer = TechnologySerializer(techs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def project_api_view(request, pk):
    project = get_object_or_404(Project, pk=pk)
    serializer = ProjectDetailSerializer(project)
    return Response(serializer.data, status=status.HTTP_200_OK)
