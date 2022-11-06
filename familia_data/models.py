from django.db import models

# Create your models here.

from django.db.models.fields import CharField, IntegerField, DateField


class FamiliaDataModel(models.Model):
    edad = IntegerField()
    nombre = CharField(max_length=100)
    apellido = CharField(max_length=100)
    fecha_nac = DateField()
    
    