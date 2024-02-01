from rest_framework.routers import DefaultRouter
from .views import LinkViewSet


router = DefaultRouter()
router.register("links", LinkViewSet)

urlpatterns = router.urls
