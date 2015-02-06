# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Partidos


#Configuracion del Modelo Partidos en la vista Administrador (vista,filtros,busqueda)
class PartidosAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Informacion Principal', {'fields': ['n_partidos', 'siglas', 'foto_partido']}),
        ('Responsable ', {'fields': ['nom_presidente', 'ape_presidente']}),
        ('Contacto', {'fields': ['correo',  'twitter', 'telefono']}),
        ('Auditoria', {'fields': ['user_create', 'user_update', ]}),
        ]
    list_display = ('siglas', 'n_partidos', 'telefono', 'correo', 'twitter')  # Muesta el str de los campos en la vista
    list_filter = ['siglas']  # Crea un fitro y definimos en base a cuales campos filtrara
    search_fields = ['siglas', 'n_partidos']  # Crea un fitro y definimos en base a cuales campos filtrara

admin.site.register(Partidos, PartidosAdmin)
