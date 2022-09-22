from django.db import models

class SuperFamiliares(models.Model):
    nombre = models.CharField(max_length=128)
    fecha_nacimiento = models.DateField()
    peso_kg = models.IntegerField()

    def __str__(self):
        return f'{self.nombre}'

    pass
