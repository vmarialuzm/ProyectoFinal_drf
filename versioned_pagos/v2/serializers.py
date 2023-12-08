from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from pagos.models import Services, PaymentUser, ExpiredPayments

class ServicesSerializer(ModelSerializer):
    class Meta:
        model = Services
        fields = "__all__"

class PaymentUserSerializer(ModelSerializer):
    service_id = PrimaryKeyRelatedField(queryset = Services.objects.all())
    class Meta:
        model = PaymentUser
        fields = "__all__"
    
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        service_id = ServicesSerializer(instance.service_id).data
        ret['service_id'] = service_id
        return ret

class ExpiredPaymentsSerializer(ModelSerializer):
    payment_user_id = PrimaryKeyRelatedField(queryset = PaymentUser.objects.all())
    class Meta:
        model = ExpiredPayments
        fields = "__all__"

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        payment_user_id = PaymentUserSerializer(instance.payment_user_id).data
        ret['payment_user_id'] = payment_user_id
        return ret