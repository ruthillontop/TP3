from django.db import models

class Pasajeros(models.Model):
    nombrepax = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    viajero_frecuente = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.nombrepax