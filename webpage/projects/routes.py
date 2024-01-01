from rest_framework.routers import DefaultRouter
from projects.views import ProjectViewSet, TechnologyViewSet

router = DefaultRouter()
router.register('projects', ProjectViewSet)
router.register('techs', TechnologyViewSet, 'techs')
urlpatterns = router.urls
