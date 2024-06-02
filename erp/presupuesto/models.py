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
    
    def _str_(self):
        return self.nombre

class Costo(models.Model):
    presupuesto = models.ForeignKey(Presupuesto, related_name='costos', on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    def _str_(self):
        return f"{self.descripcion} - {self.monto}"