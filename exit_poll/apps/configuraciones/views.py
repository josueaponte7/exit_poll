from django.shortcuts import render
from django.views.generic import TemplateView


class Configuraciones(TemplateView):
    template_name = 'configuraciones/configuraciones.html'


class Topologia(TemplateView):
    template_name = 'configuraciones/topologia.html'


class Tipos_Eleccion(TemplateView):
    template_name = 'configuraciones/categoria_eleccion.html'
