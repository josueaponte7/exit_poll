# -*- coding: utf-8 -*-
import hashlib
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, FormView
from django.contrib import messages  # Metodo para la validacion de los campos
from apps.login.forms import LoginForm
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
import datetime


def login_view(request):
    mensaje = ""
    if request.user.is_authenticated():
        return HttpResponseRedirect('/menu/')
    else:
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                usuario = authenticate(username=username, password=password)
                if usuario is not None and usuario.is_active:
                    login(request,usuario)
                    return HttpResponseRedirect('/menu/')
                else:
                    mensaje = "Usuario y/o Contraseña incorrecto"
        form = LoginForm()
        ctx = {'form': form, 'mensaje': mensaje}
        return render_to_response('login/login.html', ctx, context_instance=RequestContext(request))


def add_user_view(request):

    return render_to_response('login/add_user.html', locals(), context_instance=RequestContext(request))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
