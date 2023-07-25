from django.db import models
from usuarios.models import User

SERVICIOS_OPTIONS = [
    ("N", "Netflix"),
    ("A", "Amazon Video"),
    ("S", "Star +"),
    ("P", "Paramount +"),
]

class Pagos(models.Model):
    usuario_id = models.ForeignKey(User, on_delete=models.CASCADE)
    servicio = models.CharField(max_length=1, choices=SERVICIOS_OPTIONS)
    monto = models.FloatField()
    fecha_pago = models.DateField()

    class Meta:
        db_table = "pagos"

# modelos de la versión 2

class Services(models.Model):
    name = models.CharField(max_length=1, choices=SERVICIOS_OPTIONS)
    description = models.TextField()
    logo = models.URLField()

    class Meta:
        db_table = "services"

class PaymentUser(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    service_id = models.ForeignKey(Services, on_delete=models.CASCADE)
    amount = models.FloatField()
    payment_date = models.DateField()
    expiration_date = models.DateField()

    class Meta:
        db_table = "payment_user"

class ExpiredPayments(models.Model):
    payment_user_id = models.ForeignKey(PaymentUser, on_delete=models.CASCADE)
    penalty_fee_amount = models.FloatField()

    class Meta:
        db_table = "expired_payments"




