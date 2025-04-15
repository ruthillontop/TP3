from django.db import models

class Empleados (models.Model):
    nombreempleado = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    antiguedad = models.IntegerField()
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.nombreempleado