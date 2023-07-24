from rest_framework.serializers import ModelSerializer
from pagos.models import Pagos

class PagoSerializer(ModelSerializer):
    class Meta:
        model = Pagos
        fields = "__all__"