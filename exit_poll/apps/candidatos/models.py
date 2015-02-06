# -*- coding: utf-8 -*-
from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from apps.tipos.categoria_eleccion.models import Categoria
from apps.tipos.tipo_eleccion.models import Tipo_eleccion
from apps.topologia.estados.models import Estado
from apps.topologia.municipios.models import Municipio
from apps.topologia.parroquias.models import Parroquia
from apps.partidos.models import Partidos
from apps.elecciones.models import Eleccion
from apps.circuitos.models import Circuito
from django.contrib.auth.models import User

#Diccionario
SEXO = (
    ('0', "Femenino"),
    ('1', "Masculino"),
)


class Candidatos(models.Model):
    '''Informacion del Candidato'''
    #Informacion Principal
    nombre = models.CharField(verbose_name="Nombre del Candidato", max_length=100)
    apellido = models.CharField(verbose_name="Apellido del Candidato", max_length=100)
    cedula = models.CharField(max_length=8, verbose_name="Cédula", unique=True)
    foto = models.ImageField()
    sexo = models.CharField(choices=SEXO, default=0, max_length=15)
    edad = models.IntegerField()
    twitter = models.CharField(max_length=200, unique=True)
    part_politico = models.ForeignKey(Partidos, verbose_name="Partido Político")

    #Datos de la Elección
    tipo_eleccion = models.ForeignKey(Categoria, verbose_name="Tipo de Elección")
    tipo_candidatura = ChainedForeignKey(Tipo_eleccion, chained_field="tipo_eleccion", chained_model_field="categoria",
                                         show_all=False, auto_choose=True)
    eleccion = ChainedForeignKey(Eleccion, chained_field="tipo_candidatura", chained_model_field="tipo_eleccion",
                                 show_all=False, auto_choose=True, null=True)

    #Informacion Geográfica
    estado = models.ForeignKey(Estado, null=True)
    circuito = models.ForeignKey(Circuito, null=True)
    municipio = ChainedForeignKey(Municipio, chained_field="estado", chained_model_field="estado", show_all=False,
                                  auto_choose=True, null=True)
    parroquia = ChainedForeignKey(Parroquia, chained_field="municipio", chained_model_field="municipio", show_all=False,
                                  auto_choose=True, null=True)

    #Auditoria
    user_create = models.ForeignKey(User, null=True, blank=True, related_name='+')
    user_update = models.ForeignKey(User, null=True, blank=True, related_name='+')
    fecha_create = models.DateTimeField(auto_now_add=True, auto_now=False)
    fecha_update = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    class Meta:
        unique_together = ("cedula", "nombre", "apellido")
        ordering = ('nombre', 'apellido')

    def __unicode__(self):
        #return: Representacion en cadena de la clase Partidos
        return self.nombre

    def get_absolute_url(self):
        return ('listar_candidatos', [self.id, ])
