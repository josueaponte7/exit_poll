from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render_to_response
from django.template import RequestContext


class Menu(TemplateView):
    template_name = 'base.html'
