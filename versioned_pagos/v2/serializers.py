from rest_framework.serializers import ModelSerializer
from pagos.models import Services, PaymentUser, ExpiredPayments

class ServicesSerializer(ModelSerializer):
    class Meta:
        model = Services
        fields = "__all__"

class PaymentUserSerializer(ModelSerializer):
    class Meta:
        model = PaymentUser
        fields = "__all__"

class ExpiredPaymentsSerializer(ModelSerializer):
    class Meta:
        model = ExpiredPayments
        fields = "__all__"