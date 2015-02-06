from django.contrib import admin
from .models import Estado


class EstadoAdmin(admin.ModelAdmin):
    list_display = ('estado',)
    search_fields = ['estado', ]

admin.site.register(Estado, EstadoAdmin)
