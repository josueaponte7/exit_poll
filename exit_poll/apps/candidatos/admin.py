# -*- coding: utf-8 -*-
from django.contrib import admin
from apps.candidatos.models import Candidatos


#Configuracion del Modelo Candidatos en la vista Administrador (vista,filtros,busqueda)
class CandidatosAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Información Principal', {'fields': ['nombre', 'apellido', 'cedula', 'sexo', 'edad', 'foto', 'twitter', 'part_politico' ]}),
        ('Información de la Elección', {'fields': ['tipo_eleccion',  'tipo_candidatura', 'eleccion' ]}),
        ('Información Geográfica', {'fields': ['estado', 'circuito', 'municipio', 'parroquia' ]}),
        ('Auditoria', {'fields': ['user_create', 'user_update', ]}),
        ]
    list_display = ('cedula', 'nombre', 'apellido', 'sexo', 'tipo_candidatura', 'eleccion', 'twitter') #Muesta el str de los campos en la vista lista
    list_filter = ['part_politico', 'tipo_eleccion', 'tipo_candidatura'] #Crea un fitro y definimos en base a cuales campos filtrara
    search_fields = ['cedula', 'nombre', 'apellido'] #Crea un fitro y definimos en base a cuales campos filtrara
    
admin.site.register(Candidatos, CandidatosAdmin)