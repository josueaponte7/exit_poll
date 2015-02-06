#encoding:utf-8
from django.forms import ModelForm
from django import forms
from apps.centro_votacion.models import Centros


class CentrosForm(forms.ModelForm):

    class Meta:
        model = Centros
