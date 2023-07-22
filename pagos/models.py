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


