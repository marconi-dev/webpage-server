from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import (
    Study,
    Article,
)
from .serializers.serializers import (
    LatestStudySerializer,
    LatestArticleSerializer,
)


# @api_view(['GET'])
# def tech_api_view(request):
#     """Techs used by me in at least one project"""
#     techs = (
#         Technology.objects
#         .annotate(tech_count=Count('techs'))
#         .filter(tech_count__gt=0, techs__is_equipe_tech=False)
#         .order_by('-tech_count', 'name')
#         .values('name', 'id', 'tech_count')
#     )
#     serializer = TechnologySerializer(techs, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)

# @api_view(['GET'])
# def project_api_view(request, pk):
#     project = get_object_or_404(Project, pk=pk)
#     serializer = ProjectDetailSerializer(project)
#     return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def articles_latest_api_view(request):
    """Lists latest articles"""
    articles = Article.objects.all()[:3]
    serializer = LatestArticleSerializer(articles, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def studies_latest_api_view(request):
    """Lists latest studies"""
    studies = Study.objects.all()[:3]
    serializer = LatestStudySerializer(studies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
