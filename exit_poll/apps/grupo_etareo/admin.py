from django.contrib import admin
from apps.grupo_etareo.models import Grupo_Etareo


#Configuracion de los Modelo grupo etareo en la vista Administrador (vista,filtros,busqueda)

class Grupo_EtareoAdmin(admin.ModelAdmin):
    fieldsets =[
        ('Grupos', {'fields': ['descripcion', 'grupo_etareo']}),
    ]
    list_display = ('descripcion', 'grupo_etareo', 'user_create', 'user_update', 'fecha_create', 'fecha_update')  # Muesta el str de los campos en la vista lista
    search_fields = ['grupo_etareo', ]  # Crea un campo para busqueda directa


admin.site.register(Grupo_Etareo, Grupo_EtareoAdmin)
