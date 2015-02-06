# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


# Modelo Partidos
# Donde se registra cada uno de los partidos políticos del país 
class Partidos(models.Model):
    '''Informacion Solicitada para registrar el partido'''
    n_partidos = models.CharField(verbose_name="Nombre del Partido",  max_length=150, unique=True)
    siglas = models.CharField(max_length=10, unique=True)
    foto_partido = models.ImageField()
    nom_presidente = models.CharField(verbose_name="Nombre del Presidente", max_length=100, unique=True)
    ape_presidente = models.CharField(verbose_name="Apellido del Presidente", max_length=100, unique=True)
    correo = models.EmailField(max_length=200, unique=True)
    twitter = models.CharField(max_length=200, unique=True)
    telefono = models.CharField(max_length=11, verbose_name="Teléfono", unique=True)

    user_create = models.ForeignKey(User, null=True, blank=True, related_name='+')
    user_update = models.ForeignKey(User, null=True, blank=True, related_name='+')
    fecha_create = models.DateTimeField(auto_now_add=True, auto_now=False)
    fecha_update = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    class Meta:
        unique_together = ("n_partidos", "siglas")
        ordering = ('n_partidos', 'siglas')

    def __unicode__(self):
        #return: Representacion en cadena de la clase Partidos
        return self.siglas

    def get_absolute_url(self):
        return ('listar_partido', [self.id, ])
