from rest_framework.routers import DefaultRouter

from .views import PostApiViewSet

api_name = 'api'

router = DefaultRouter()
router.register(prefix='api/v1/posts', viewset=PostApiViewSet, basename='post')

urlpatterns = router.urls
