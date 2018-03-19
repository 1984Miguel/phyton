# -*- coding:utf -*-

from django.db import models

# Create your models here.

VENTAS = 'VEN'
POXIMAS = 'PRO'
ENTREGADAS = 'ENT'

TIPO = (
    (VENTAS, "Promociones en venta"),
    (POXIMAS, "Promociones próximas"),
    (ENTREGADAS, "Promociones entregadas")


)



class Promocion(models.Model):


    titulo = models.CharField(max_length=150)
    url = models.TextField()
    descripcion = models.TextField()
    municipio = models.CharField(max_length=150)
    entrega = models.DateTimeField(blank=True , null=True)
    #modificado = models.DateTimeField(auto_now.add=True)
    tipo = models.CharField(max_length=3, choices=TIPO)
    banner = models.BooleanField(default=False)
    precio = models.IntegerField(blank=True , null=True)

    dormitorios = models.CharField(max_length=150,blank=True, null=True)
    def __unicode__(self):
        return self.titulo
