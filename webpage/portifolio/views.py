from django.db.models import Q
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Profile, Project, Technology
from .serializers import ProfileSerializer, ProjectSerializer


@api_view(['GET'])
def profile_view(request):
    profile = Profile.objects.prefetch_related('links').first()
    serializer = ProfileSerializer(profile)
    return Response(serializer.data, status=status.HTTP_200_OK)   


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
            # TODO Provide a hashmap eg. {tech_name: UUID} to the client 
            # then filter against UUIDs directly
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
