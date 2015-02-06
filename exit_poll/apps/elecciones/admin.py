# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Eleccion


#Configuracion del Modelo Eleccion en la vista Administrador (vista,filtros,busqueda)
class EleccionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Informacion Principal', {'fields': ['nombre', 'categoria_eleccion', 'tipo_eleccion', 'year_eleccion']}),
        ('Auditoria', {'fields': ['user_create', 'user_update', ]}),
                ]

    list_display = ['nombre', 'categoria_eleccion', 'tipo_eleccion', 'year_eleccion']  # Muesta el str de los campos en la vista lista
    list_filter = ['year_eleccion', 'categoria_eleccion', 'tipo_eleccion']  # Crea un fitro y definimos en base a cuales campos filtrara
    search_fields = ['nombre', 'tipo_eleccion', 'tipo_candidatura', 'year_eleccion']  # Crea un fitro y definimos en base a cuales campos filtrara

admin.site.register(Eleccion, EleccionAdmin)
