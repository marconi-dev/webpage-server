from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Article
from .serializers import (
    ArticleSerializer, 
    LatestArticleSerializer
)

# Create your views here.
class ArticleViewSet(ReadOnlyModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    @action(['GET'], detail=False)
    def latest(self, request, *args, **kwargs):
        latest_queryset = self.get_queryset()[:3] # 3 fisrt items
        serializer = LatestArticleSerializer(latest_queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
