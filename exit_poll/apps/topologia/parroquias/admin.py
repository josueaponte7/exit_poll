from django.contrib import admin
from .models import Parroquia


class ParroquiaAdmin(admin.ModelAdmin):
    list_display = ('estado', 'municipio', 'parroquia') #Muesta el str de los campos en la vista lista
    list_filter = ['estado', 'municipio'] #Crea un fitro y definimos en base a cuales campos filtrara
    search_fields = ['parroquia'] #Crea un campo para busqueda directa

admin.site.register(Parroquia, ParroquiaAdmin)
