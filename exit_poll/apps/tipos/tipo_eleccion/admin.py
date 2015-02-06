# -*- coding: utf-8 -*-
from django.contrib import admin
from apps.tipos.tipo_eleccion.models import Tipo_eleccion


class TipoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'categoria')  # Muesta el str de los campos en la vista lista
    list_filter = ['categoria', ]  # Crea un fitro y definimos en base a cuales campos filtrara
    search_fields = ['categoria', 'tipo']  # Crea un fitro y definimos en base a cuales campos filtrara

admin.site.register(Tipo_eleccion, TipoAdmin)
