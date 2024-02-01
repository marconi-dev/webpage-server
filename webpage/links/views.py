from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Link
from .serializers import LinkSerializer


# Create your views here.
class LinkViewSet(ReadOnlyModelViewSet):
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
