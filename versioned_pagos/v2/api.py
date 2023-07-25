from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet, ModelViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle
from pagos.models import Services, PaymentUser, ExpiredPayments
from .serializers import ServicesSerializer, PaymentUserSerializer, ExpiredPaymentsSerializer

class ServicesViewSet(ReadOnlyModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

class PaymentUserViewSet(ModelViewSet):
    queryset = PaymentUser.objects.all()
    serializer_class = PaymentUserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['payment_date','expiration_date']
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    def perform_create(self, serializer):
        payment_date = serializer.validated_data['payment_date']
        expiration_date = serializer.validated_data['expiration_date']

        if payment_date > expiration_date:
            # Calcula la penalización como el 10% del monto (amount)
            penalty_fee_amount = serializer.validated_data['amount'] * 0.10

            expired_payment = serializer.save()

            # Crea un registro en ExpiredPayments con los datos necesarios
            ExpiredPayments.objects.create(
                payment_user_id = expired_payment,
                penalty_fee_amount = penalty_fee_amount,
            )

        else:

            # Finalmente, guarda el PaymentUser en la base de datos
            serializer.save()

class CreateListRetrieveExpiredPaymentsViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin,GenericViewSet):
    queryset = ExpiredPayments.objects.all()
    serializer_class = ExpiredPaymentsSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    def list(self, request, *args, **kwards):    #para hacer referencia al mixin
        return super().list(request, *args, **kwards)
    
    def retrieve(self, request, *args, **kwards):    
        return super().retrieve(request, *args, **kwards)
    
    def create(self, request, *args, **kwards):    
        return super().create(request, *args, **kwards)