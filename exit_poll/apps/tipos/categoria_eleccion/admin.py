# -*- coding: utf-8 -*-
from django.contrib import admin
from apps.tipos.categoria_eleccion.models import Categoria


#Configuracion de los Modelos Cetegoria(de Eleccion) y Tipo(de acuerdo a la categoria) en la vista Administrador (vista,filtros,busqueda)
class CategoriaAdmin(admin.ModelAdmin):
    fieldsets =[
        ('Categorias', {'fields': ['categoria',]}),
    ]
    list_display = ('categoria', 'user_create', 'user_update', 'fecha_create', 'fecha_update')  # Muesta el str de los campos en la vista lista
    search_fields = ['categoria', ]  # Crea un fitro y definimos en base a cuales campos filtrara

admin.site.register(Categoria, CategoriaAdmin)
