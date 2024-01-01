from rest_framework.routers import DefaultRouter
from .views import StudyViewSet


router = DefaultRouter()
router.register('studies', StudyViewSet)

urlpatterns = router.urls
