# En tu archivo models.py dentro de la app contabilidad_personal

from django.db import models

class Gasto(models.Model):
    TIPOS_GASTO = [
        ('seguro', 'Seguro'),
        ('alquiler', 'Alquiler'),
        ('servicio', 'Servicio'),
        ('comida', 'Comida'),
        ('gasolina', 'Gasolina'),
        ('carro', 'Carro'),
        ('condominio', 'Condominio'),
        ('educacion', 'Educación'),
        ('ocio', 'Ocio'),
        ('reparaciones', 'Reparaciones'),
        ('impuestos', 'Impuestos'),
        ('otro', 'Otro'),
    ]

    fecha = models.DateField()
    concepto = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPOS_GASTO)
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Gasto de {self.concepto} por {self.monto} en {self.fecha}"


class Presupuesto(models.Model):
    mes = models.CharField(max_length=20)
    año = models.IntegerField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Presupuesto de gastos del mes {self.mes} del año {self.año}"


class Ingreso(models.Model):
    fecha = models.DateField()
    concepto = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Ingreso de {self.concepto} por {self.monto} en {self.fecha}"