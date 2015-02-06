from django.contrib import admin
from .models import Municipio


class MunicipioAdmin(admin.ModelAdmin):
    list_display = ('estado', 'municipio') #Muesta el str de los campos en la vista lista
    list_filter = ['municipio',] #Crea un fitro y definimos en base a cuales campos filtrara
    search_fields = ['estado', 'municipio']#Crea un campo para busqueda directa

admin.site.register(Municipio, MunicipioAdmin)

