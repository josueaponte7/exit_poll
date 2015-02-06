from django.contrib import admin
from .models import Centros


#Configuracion del Modelo Centros(de votacion) en la vista Administrador
class CentrosAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Informacion Principal', {'fields': ['codigo', 'nombre']}),
        ('Ubicacion', {'fields': ['estado',  'municipio', 'parroquia','direccion', ]}),
        ('Auditoria', {'fields': ['user_create', 'user_update', ]}),
        ]
    list_display = ('codigo', 'nombre', 'estado', 'municipio', 'parroquia') #Muesta el str de los campos en la vista lista
    list_filter = ['estado'] #Crea un fitro y definimos en base a cuales campos filtrara
    search_fields = ['codigo', 'nombre'] #Crea un fitro y definimos en base a cuales campos filtrara

admin.site.register(Centros, CentrosAdmin)