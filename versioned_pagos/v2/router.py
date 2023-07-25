from .api import ServicesViewSet, PaymentUserViewSet, CreateListRetrieveExpiredPaymentsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"services", ServicesViewSet, basename="services")
router.register(r"payment_user", PaymentUserViewSet, basename="payment_user")
router.register(r"expired_payments", CreateListRetrieveExpiredPaymentsViewSet, basename="expired_payments")

api_urlpatterns = router.urls