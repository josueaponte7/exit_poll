#encoding:utf-8
from django.forms import ModelForm
from django import forms
from .models import Estado


class EstadoForm(forms.ModelForm):

    class Meta:
        model = Estado
