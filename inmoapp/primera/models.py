# -*- coding:utf -*-

from django.db import models

# Create your models here.


class Presentacion(models.Model):

    nombre = models.TextField()
    descripcion = models.TextField()


    def __unicode__(self):
        return self.nombre