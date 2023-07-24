from rest_framework.routers import DefaultRouter
from .api import CreateListRetrieveViewSet

router = DefaultRouter()

router.register(r"pagos", CreateListRetrieveViewSet, basename="pagos")

api_urlpatterns = router.urls