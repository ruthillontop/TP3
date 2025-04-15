from django.db import models

# Create your models here.

class Destinos(models.Model):
    ciudad = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    

    def __str__(self):
        return self.pais