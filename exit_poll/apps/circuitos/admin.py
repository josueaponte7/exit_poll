from django.contrib import admin
from .models import Circuito


class CircuitosAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Informacion Principal', {'fields': ['estado', 'n_circuito', 'municipio', 'num_max_candidatos']}),
        ('Auditoria', {'fields': ['user_create', 'user_update']}),
        ]
    list_display = ('estado', 'n_circuito', 'num_max_candidatos', 'fecha_create', 'fecha_update')  # Muesta el str de los campos en la vista lista
    list_filter = ['estado']  # Crea un fitro y definimos en base a cuales campos filtrara
    search_fields = ['estado', 'n_circuito']  # Crea un fitro y definimos en base a cuales campos filtrara

admin.site.register(Circuito, CircuitosAdmin)
