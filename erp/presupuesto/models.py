from django.db import models

class Administrador(models.Model):
    nombre = models.CharField(max_length=255)
    contraseña = models.CharField(max_length=255)

class SolicitudPresupuesto(models.Model):
    fecha = models.DateField()
    aprobacion = models.BooleanField()
    administrador = models.ForeignKey(Administrador, on_delete=models.CASCADE)

class Presupuesto(models.Model):
    fecha_inicio = models.DateField()
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_limite = models.DateField()
    gastos = models.DecimalField(max_digits=10, decimal_places=2)
    solicitud_presupuesto = models.OneToOneField(SolicitudPresupuesto, on_delete=models.CASCADE)
