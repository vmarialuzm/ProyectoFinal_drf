from rest_framework.routers import DefaultRouter
from .views import CreateListRetrieveViewSet

pagos_router =DefaultRouter()

pagos_router.register(r"v1/api", CreateListRetrieveViewSet, basename="pagos")

urlpatterns = pagos_router.urls