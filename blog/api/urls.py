from rest_framework.routers import DefaultRouter

from .views import PostApiViewSet, BookApiViewSet

api_name = 'api'

router = DefaultRouter()
router.register(prefix='posts', viewset=PostApiViewSet, basename='post')
router.register(prefix='books', viewset=BookApiViewSet, basename='book')

urlpatterns = router.urls
