from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle
from django_filters.rest_framework import DjangoFilterBackend
from pagos.models import Pagos
from .serializers import PagoSerializer
from .pagination import SimplePagination

class CreateListRetrieveViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin,GenericViewSet):
    queryset = Pagos.objects.all()
    serializer_class = PagoSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = SimplePagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['usuario_id','fecha_pago','servicio']

    throttle_classes = [UserRateThrottle]

    def list(self, request, *args, **kwards):    #para hacer referencia al mixin
        return super().list(request, *args, **kwards)
    
    def retrieve(self, request, *args, **kwards):    
        return super().retrieve(request, *args, **kwards)
    
    def create(self, request, *args, **kwards):    
        return super().create(request, *args, **kwards)