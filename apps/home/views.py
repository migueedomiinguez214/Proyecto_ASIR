# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.template import loader
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import render
from .models import *
from datetime import datetime
from itertools import chain
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
import os
import csv



@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

#VISTAS DE COCINA

class ComidaListView1(ListView):
    template_name = 'ui-cocina.edu.1.html'
    queryset = Comida.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = datetime.now().date()
        context['comidas'] = Comida.objects.filter(id_carrito=1, fecha__date=today)
        context['postres'] = Postre.objects.filter(id_carrito=1, fecha__date=today)
        return context

class ComidaListView2(ListView):
    template_name = 'ui-cocina.edu.2.html'
    queryset = Comida.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = datetime.now().date()
        context['comidas'] = Comida.objects.filter(id_carrito=2, fecha__date=today)
        context['postres'] = Postre.objects.filter(id_carrito=2, fecha__date=today)
        return context

class ComidaListView3(ListView):
    template_name = 'ui-cocina.edu.3.html'
    queryset = Comida.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = datetime.now().date()
        context['comidas'] = Comida.objects.filter(id_carrito=3, fecha__date=today)
        context['postres'] = Postre.objects.filter(id_carrito=3, fecha__date=today)
        return context

class ComidaListView4(ListView):
    template_name = 'ui-cocina.edu.4.html'
    queryset = Comida.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = datetime.now().date()
        context['comidas'] = Comida.objects.filter(id_carrito=4, fecha__date=today)
        context['postres'] = Postre.objects.filter(id_carrito=4, fecha__date=today)
        return context

class ComidaListView5(ListView):
    template_name = 'ui-cocina.edu.5.html'
    queryset = Comida.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = datetime.now().date()
        context['comidas'] = Comida.objects.filter(id_carrito=5, fecha__date=today)
        context['postres'] = Postre.objects.filter(id_carrito=5, fecha__date=today)
        return context

class ComidaListView6(ListView):
    template_name = 'ui-cocina.edu.6.html'
    queryset = Comida.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = datetime.now().date()
        context['comidas'] = Comida.objects.filter(id_carrito=6, fecha__date=today)
        context['postres'] = Postre.objects.filter(id_carrito=6, fecha__date=today)
        return context

class ComidaListView7(ListView):
    template_name = 'ui-cocina.resi.7.html'
    queryset = Comida.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = datetime.now().date()
        context['comidas'] = Comida.objects.filter(id_carrito=7, fecha__date=today)
        context['postres'] = Postre.objects.filter(id_carrito=7, fecha__date=today)
        return context

class ComidaListView8(ListView):
    template_name = 'ui-cocina.resi.8.html'
    queryset = Comida.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = datetime.now().date()
        context['comidas'] = Comida.objects.filter(id_carrito=8, fecha__date=today)
        context['postres'] = Postre.objects.filter(id_carrito=8, fecha__date=today)
        return context

class ComidaListView9(ListView):
    template_name = 'ui-cocina.ocu.html'
    queryset = Comida.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = datetime.now().date()
        context['comidas'] = Comida.objects.filter(id_carrito=9, fecha__date=today)
        context['postres'] = Postre.objects.filter(id_carrito=9, fecha__date=today)
        return context

class ComidaListView10(ListView):
    template_name = 'ui-cocina.unid.10.html'
    queryset = Comida.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = datetime.now().date()
        context['comidas'] = Comida.objects.filter(id_carrito=10, fecha__date=today)
        context['postres'] = Postre.objects.filter(id_carrito=10, fecha__date=today)
        return context

class ComidaListView11(ListView):
    template_name = 'ui-cocina.unid.11.html'
    queryset = Comida.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = datetime.now().date()
        context['comidas'] = Comida.objects.filter(id_carrito=11, fecha__date=today)
        context['postres'] = Postre.objects.filter(id_carrito=11, fecha__date=today)
        return context

#VISTA DE UpdateView

class ComidaUpdateView1(UpdateView):
    model = Comida
    fields = ["tipo_comida", "dieta_aler_otro", "sal", "observaciones", "cantidad"]
    template_name = 'ui-cocina.edu.1.edit.html'
    success_url = reverse_lazy('comida_list_1')
   
class ComidaUpdateView2(UpdateView):
    model = Comida
    fields = ["tipo_comida", "dieta_aler_otro", "sal", "observaciones", "cantidad"]
    template_name = 'ui-cocina.edu.1.edit.html'
    success_url = reverse_lazy('comida_list_2')

class ComidaUpdateView3(UpdateView):
    model = Comida
    fields = ["tipo_comida", "dieta_aler_otro", "sal", "observaciones", "cantidad"]
    template_name = 'ui-cocina.edu.1.edit.html'
    success_url = reverse_lazy('comida_list_3')

class ComidaUpdateView4(UpdateView):
    model = Comida
    fields = ["tipo_comida", "dieta_aler_otro", "sal", "observaciones", "cantidad"]
    template_name = 'ui-cocina.edu.1.edit.html'
    success_url = reverse_lazy('comida_list_4')

class ComidaUpdateView5(UpdateView):
    model = Comida
    fields = ["tipo_comida", "dieta_aler_otro", "sal", "observaciones", "cantidad"]
    template_name = 'ui-cocina.edu.1.edit.html'
    success_url = reverse_lazy('comida_list_5')

class ComidaUpdateView6(UpdateView):
    model = Comida
    fields = ["tipo_comida", "dieta_aler_otro", "sal", "observaciones", "cantidad"]
    template_name = 'ui-cocina.edu.1.edit.html'
    success_url = reverse_lazy('comida_list_6')

class ComidaUpdateView7(UpdateView):
    model = Comida
    fields = ["tipo_comida", "dieta_aler_otro", "sal", "observaciones", "cantidad"]
    template_name = 'ui-cocina.edu.1.edit.html'
    success_url = reverse_lazy('comida_list_7')

class ComidaUpdateView8(UpdateView):
    model = Comida
    fields = ["tipo_comida", "dieta_aler_otro", "sal", "observaciones", "cantidad"]
    template_name = 'ui-cocina.edu.1.edit.html'
    success_url = reverse_lazy('comida_list_8')

class ComidaUpdateView9(UpdateView):
    model = Comida
    fields = ["tipo_comida", "dieta_aler_otro", "sal", "observaciones", "cantidad"]
    template_name = 'ui-cocina.edu.1.edit.html'
    success_url = reverse_lazy('comida_list_9')

class ComidaUpdateView10(UpdateView):
    model = Comida
    fields = ["tipo_comida", "dieta_aler_otro", "sal", "observaciones", "cantidad"]
    template_name = 'ui-cocina.edu.1.edit.html'
    success_url = reverse_lazy('comida_list_10')

class ComidaUpdateView11(UpdateView):
    model = Comida
    fields = ["tipo_comida", "dieta_aler_otro", "sal", "observaciones", "cantidad"]
    template_name = 'ui-cocina.edu.1.edit.html'
    success_url = reverse_lazy('comida_list_11')

#POSTRE UpdateView

class PostreUpdateView1(UpdateView):
    model = Postre
    fields = ["tipo_postre", "cantidad"]
    template_name = 'ui-cocina.edu.1.edit.html'
    success_url = reverse_lazy('comida_list_1')

class PostreUpdateView2(UpdateView):
    model = Postre
    fields = ["tipo_postre", "cantidad"]
    template_name = 'ui-cocina.edu.1.edit.html'
    success_url = reverse_lazy('comida_list_2')

class PostreUpdateView3(UpdateView):
    model = Postre
    fields = ["tipo_postre", "cantidad"]
    template_name = 'ui-cocina.edu.1.edit.html'
    success_url = reverse_lazy('comida_list_3')

class PostreUpdateView4(UpdateView):
    model = Postre
    fields = ["tipo_postre", "cantidad"]
    template_name = 'ui-cocina.edu.1.edit.html'
    success_url = reverse_lazy('comida_list_4')

class PostreUpdateView5(UpdateView):
    model = Postre
    fields = ["tipo_postre", "cantidad"]
    template_name = 'ui-cocina.edu.1.edit.html'
    success_url = reverse_lazy('comida_list_5')

class PostreUpdateView6(UpdateView):
    model = Postre
    fields = ["tipo_postre", "cantidad"]
    template_name = 'ui-cocina.edu.1.edit.html'
    success_url = reverse_lazy('comida_list_6')

class PostreUpdateView7(UpdateView):
    model = Postre
    fields = ["tipo_postre", "cantidad"]
    template_name = 'ui-cocina.edu.1.edit.html'
    success_url = reverse_lazy('comida_list_7')

class PostreUpdateView8(UpdateView):
    model = Postre
    fields = ["tipo_postre", "cantidad"]
    template_name = 'ui-cocina.edu.1.edit.html'
    success_url = reverse_lazy('comida_list_8')

class PostreUpdateView9(UpdateView):
    model = Postre
    fields = ["tipo_postre", "cantidad"]
    template_name = 'ui-cocina.edu.1.edit.html'
    success_url = reverse_lazy('comida_list_9')

class PostreUpdateView10(UpdateView):
    model = Postre
    fields = ["tipo_postre", "cantidad"]
    template_name = 'ui-cocina.edu.1.edit.html'
    success_url = reverse_lazy('comida_list_10')

class PostreUpdateView11(UpdateView):
    model = Postre
    fields = ["tipo_postre", "cantidad"]
    template_name = 'ui-cocina.edu.1.edit.html'
    success_url = reverse_lazy('comida_list_11')

#VISTAS GENERICAS


def page_user(request):
    return render(request, 'page-user.html')

def educacion(request):
    return render(request, 'ui-Educacion.html')

def cocina(request):
    return render(request, 'ui-cocina.html')

def cocinaedu(request):
    return render(request, 'ui-cocina.edu.html')

def cocinaresi(request):
    return render(request, 'ui-cocina.resi.html')

def cocinaocu(request):
    return render(request, 'ui-cocina.ocu.html')

def cocinaunid(request):
    return render(request, 'ui-cocina.unid.html')

def residencias(request):
    return render(request, 'ui-Residencia.html')

def ocupacional(request):
    return render(request, 'ui-Ocupacional.html')

def unidaddia(request):
    return render(request, 'ui-UnidadDia.html')

#VISTAS DE CREAR


class Comida1CreateView(SuccessMessageMixin, CreateView):
    model = Comida
    fields = ['tipo_comida', 'dieta_aler_otro', 'sal', 'observaciones', 'cantidad']
    template_name = 'ui-Educacion.1.html'
    success_url = reverse_lazy('crear_carrito1')  # Reemplaza 'nombre_de_la_vista' con el nombre de tu vista
    success_message = 'La comida se agregó correctamente'

    def form_valid(self, form):
        # Establecer id_carrito como 1
        form.instance.id_carrito = 1
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Filtrar las comidas por la fecha de hoy
        today = datetime.now().date()
        comidas_hoy = Comida.objects.filter(id_carrito=1,fecha__date=today)
        context['comidas_hoy'] = comidas_hoy
        return context

    

class Comida2CreateView(CreateView):
    model = Comida
    fields = ['tipo_comida', 'dieta_aler_otro', 'sal', 'observaciones', 'cantidad']
    template_name = 'ui-Educacion.2.html'
    success_url = reverse_lazy('crear_carrito2')  # Reemplaza 'nombre_de_la_vista' con el nombre de tu vista

    def form_valid(self, form):
        # Establecer id_carrito como 1
        form.instance.id_carrito = 2
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Filtrar las comidas por la fecha de hoy
        today = datetime.now().date()
        comidas_hoy = Comida.objects.filter(id_carrito=2,fecha__date=today)
        context['comidas_hoy'] = comidas_hoy
        return context

class Comida3CreateView(CreateView):
    model = Comida
    fields = ['tipo_comida', 'dieta_aler_otro', 'sal', 'observaciones', 'cantidad']
    template_name = 'ui-Educacion.3.html'
    success_url = reverse_lazy('crear_carrito3')  # Reemplaza 'nombre_de_la_vista' con el nombre de tu vista

    def form_valid(self, form):
        # Establecer id_carrito como 1
        form.instance.id_carrito = 3
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Filtrar las comidas por la fecha de hoy
        today = datetime.now().date()
        comidas_hoy = Comida.objects.filter(id_carrito=3,fecha__date=today)
        context['comidas_hoy'] = comidas_hoy
        return context


class Comida4CreateView(CreateView):
    model = Comida
    fields = ['tipo_comida', 'dieta_aler_otro', 'sal', 'observaciones', 'cantidad']
    template_name = 'ui-Educacion.4.html'
    success_url = reverse_lazy('crear_carrito4')  # Reemplaza 'nombre_de_la_vista' con el nombre de tu vista

    def form_valid(self, form):
        # Establecer id_carrito como 1
        form.instance.id_carrito = 4
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Filtrar las comidas por la fecha de hoy
        today = datetime.now().date()
        comidas_hoy = Comida.objects.filter(id_carrito=4,fecha__date=today)
        context['comidas_hoy'] = comidas_hoy
        return context

class Comida5CreateView(CreateView):
    model = Comida
    fields = ['tipo_comida', 'dieta_aler_otro', 'sal', 'observaciones', 'cantidad']
    template_name = 'ui-Educacion.5.html'
    success_url = reverse_lazy('crear_carrito5')  # Reemplaza 'nombre_de_la_vista' con el nombre de tu vista

    def form_valid(self, form):
        # Establecer id_carrito como 1
        form.instance.id_carrito = 5
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Filtrar las comidas por la fecha de hoy
        today = datetime.now().date()
        comidas_hoy = Comida.objects.filter(id_carrito=5,fecha__date=today)
        context['comidas_hoy'] = comidas_hoy
        return context
   

class Comida6CreateView(CreateView):
    model = Comida
    fields = ['tipo_comida', 'dieta_aler_otro', 'sal', 'observaciones', 'cantidad']
    template_name = 'ui-Educacion.6.html'
    success_url = reverse_lazy('crear_carrito6')  # Reemplaza 'nombre_de_la_vista' con el nombre de tu vista

    def form_valid(self, form):
        # Establecer id_carrito como 1
        form.instance.id_carrito = 6
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Filtrar las comidas por la fecha de hoy
        today = datetime.now().date()
        comidas_hoy = Comida.objects.filter(id_carrito=6,fecha__date=today)
        context['comidas_hoy'] = comidas_hoy
        return context


class Comida7CreateView(CreateView):
    model = Comida
    fields = ['tipo_comida', 'dieta_aler_otro', 'sal', 'observaciones', 'cantidad']
    template_name = 'ui-Educacion.7.html'
    success_url = reverse_lazy('crear_carrito7')  # Reemplaza 'nombre_de_la_vista' con el nombre de tu vista

    def form_valid(self, form):
        # Establecer id_carrito como 1
        form.instance.id_carrito = 7
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Filtrar las comidas por la fecha de hoy
        today = datetime.now().date()
        comidas_hoy = Comida.objects.filter(id_carrito=7,fecha__date=today)
        context['comidas_hoy'] = comidas_hoy
        return context


class Comida8CreateView(CreateView):
    model = Comida
    fields = ['tipo_comida', 'dieta_aler_otro', 'sal', 'observaciones', 'cantidad']
    template_name = 'ui-Educacion.8.html'
    success_url = reverse_lazy('crear_carrito8')  # Reemplaza 'nombre_de_la_vista' con el nombre de tu vista

    def form_valid(self, form):
        # Establecer id_carrito como 1
        form.instance.id_carrito = 8
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Filtrar las comidas por la fecha de hoy
        today = datetime.now().date()
        comidas_hoy = Comida.objects.filter(id_carrito=8,fecha__date=today)
        context['comidas_hoy'] = comidas_hoy
        return context


class Comida9CreateView(CreateView):
    model = Comida
    fields = ['tipo_comida', 'dieta_aler_otro', 'sal', 'observaciones', 'cantidad']
    template_name = 'ui-Educacion.9.html'
    success_url = reverse_lazy('crear_carrito9')  # Reemplaza 'nombre_de_la_vista' con el nombre de tu vista

    def form_valid(self, form):
        # Establecer id_carrito como 1
        form.instance.id_carrito = 9
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Filtrar las comidas por la fecha de hoy
        today = datetime.now().date()
        comidas_hoy = Comida.objects.filter(id_carrito=9,fecha__date=today)
        context['comidas_hoy'] = comidas_hoy
        return context


class Comida10CreateView(CreateView):
    model = Comida
    fields = ['tipo_comida', 'dieta_aler_otro', 'sal', 'observaciones', 'cantidad']
    template_name = 'ui-Educacion.10.html'
    success_url = reverse_lazy('crear_carrito10')  # Reemplaza 'nombre_de_la_vista' con el nombre de tu vista

    def form_valid(self, form):
        # Establecer id_carrito como 1
        form.instance.id_carrito = 10
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Filtrar las comidas por la fecha de hoy
        today = datetime.now().date()
        comidas_hoy = Comida.objects.filter(id_carrito=10,fecha__date=today)
        context['comidas_hoy'] = comidas_hoy
        return context


class Comida11CreateView(CreateView):
    model = Comida
    fields = ['tipo_comida', 'dieta_aler_otro', 'sal', 'observaciones', 'cantidad']
    template_name = 'ui-Educacion.11.html'
    success_url = reverse_lazy('crear_carrito11')  # Reemplaza 'nombre_de_la_vista' con el nombre de tu vista

    def form_valid(self, form):
        # Establecer id_carrito como 1
        form.instance.id_carrito = 11
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Filtrar las comidas por la fecha de hoy
        today = datetime.now().date()
        comidas_hoy = Comida.objects.filter(id_carrito=11,fecha__date=today)
        context['comidas_hoy'] = comidas_hoy
        return context


#VISTAS DE EDUCACION Postre


class Postre1CreateView(CreateView):
    model = Postre
    fields = ['tipo_postre', 'cantidad']
    template_name = 'ui-Educacion.P1.html'
    success_url = reverse_lazy('crear_carrito1')

    def form_valid(self, form):
        # Establecer id_carrito como 1
        form.instance.id_carrito = 1
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Filtrar las comidas por la fecha de hoy
        today = datetime.now().date()
        postre_hoy = Postre.objects.filter(id_carrito=1,fecha__date=today)
        context['postre_hoy'] = postre_hoy
        return context

class Postre2CreateView(CreateView):
    model = Postre
    fields = ['tipo_postre', 'cantidad']
    template_name = 'ui-Educacion.P2.html'
    success_url = reverse_lazy('crear_carrito2')

    def form_valid(self, form):
        form.instance.id_carrito = 2
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Filtrar las comidas por la fecha de hoy
        today = datetime.now().date()
        postre_hoy = Postre.objects.filter(id_carrito=2,fecha__date=today)
        context['postre_hoy'] = postre_hoy
        return context

class Postre3CreateView(CreateView):
    model = Postre
    fields = ['tipo_postre', 'cantidad']
    template_name = 'ui-Educacion.P3.html'
    success_url = reverse_lazy('crear_carrito3')

    def form_valid(self, form):
        form.instance.id_carrito = 3
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Filtrar las comidas por la fecha de hoy
        today = datetime.now().date()
        postre_hoy = Postre.objects.filter(id_carrito=3,fecha__date=today)
        context['postre_hoy'] = postre_hoy
        return context

class Postre4CreateView(CreateView):
    model = Postre
    fields = ['tipo_postre', 'cantidad']
    template_name = 'ui-Educacion.P4.html'
    success_url = reverse_lazy('crear_carrito4')

    def form_valid(self, form):
        form.instance.id_carrito = 4
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Filtrar las comidas por la fecha de hoy
        today = datetime.now().date()
        postre_hoy = Postre.objects.filter(id_carrito=4,fecha__date=today)
        context['postre_hoy'] = postre_hoy
        return context
# Repetir para los carritos 5 al 11 cambiando los números en cada clase y en las URLs de éxito

class Postre5CreateView(CreateView):
    model = Postre
    fields = ['tipo_postre', 'cantidad']
    template_name = 'ui-Educacion.P5.html'
    success_url = reverse_lazy('crear_carrito5')

    def form_valid(self, form):
        form.instance.id_carrito = 5
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Filtrar las comidas por la fecha de hoy
        today = datetime.now().date()
        postre_hoy = Postre.objects.filter(id_carrito=5,fecha__date=today)
        context['postre_hoy'] = postre_hoy
        return context

class Postre6CreateView(CreateView):
    model = Postre
    fields = ['tipo_postre', 'cantidad']
    template_name = 'ui-Educacion.P6.html'
    success_url = reverse_lazy('crear_carrito6')

    def form_valid(self, form):
        form.instance.id_carrito = 6
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Filtrar las comidas por la fecha de hoy
        today = datetime.now().date()
        postre_hoy = Postre.objects.filter(id_carrito=6,fecha__date=today)
        context['postre_hoy'] = postre_hoy
        return context

class Postre7CreateView(CreateView):
    model = Postre
    fields = ['tipo_postre', 'cantidad']
    template_name = 'ui-Educacion.P7.html'
    success_url = reverse_lazy('crear_carrito7')

    def form_valid(self, form):
        form.instance.id_carrito = 7
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Filtrar las comidas por la fecha de hoy
        today = datetime.now().date()
        postre_hoy = Postre.objects.filter(id_carrito=7,fecha__date=today)
        context['postre_hoy'] = postre_hoy
        return context

class Postre8CreateView(CreateView):
    model = Postre
    fields = ['tipo_postre', 'cantidad']
    template_name = 'ui-Educacion.P8.html'
    success_url = reverse_lazy('crear_carrito8')

    def form_valid(self, form):
        form.instance.id_carrito = 8
        return super().form_valid(form)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Filtrar las comidas por la fecha de hoy
        today = datetime.now().date()
        postre_hoy = Postre.objects.filter(id_carrito=8,fecha__date=today)
        context['postre_hoy'] = postre_hoy
        return context

class Postre9CreateView(CreateView):
    model = Postre
    fields = ['tipo_postre', 'cantidad']
    template_name = 'ui-Educacion.P9.html'
    success_url = reverse_lazy('crear_carrito9')

    def form_valid(self, form):
        form.instance.id_carrito = 9
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Filtrar las comidas por la fecha de hoy
        today = datetime.now().date()
        postre_hoy = Postre.objects.filter(id_carrito=9,fecha__date=today)
        context['postre_hoy'] = postre_hoy
        return context

class Postre10CreateView(CreateView):
    model = Postre
    fields = ['tipo_postre', 'cantidad']
    template_name = 'ui-Educacion.P10.html'
    success_url = reverse_lazy('crear_carrito10')

    def form_valid(self, form):
        form.instance.id_carrito = 10
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Filtrar las comidas por la fecha de hoy
        today = datetime.now().date()
        postre_hoy = Postre.objects.filter(id_carrito=10,fecha__date=today)
        context['postre_hoy'] = postre_hoy
        return context

class Postre11CreateView(CreateView):
    model = Postre
    fields = ['tipo_postre', 'cantidad']
    template_name = 'ui-Educacion.P11.html'
    success_url = reverse_lazy('crear_carrito11')

    def form_valid(self, form):
        form.instance.id_carrito = 11
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Filtrar las comidas por la fecha de hoy
        today = datetime.now().date()
        postre_hoy = Postre.objects.filter(id_carrito=11,fecha__date=today)
        context['postre_hoy'] = postre_hoy
        return context

#VISTAS DE DeleteView

class ComidaDeleteView1(DeleteView):
    model = Comida
    template_name = 'ui-cocina.edu.2.delete.html'
    success_url = reverse_lazy('comida_list_1')

class ComidaDeleteView2(DeleteView):
    model = Comida
    template_name = 'ui-cocina.edu.2.delete.html'
    success_url = reverse_lazy('comida_list_1')

class ComidaDeleteView3(DeleteView):
    model = Comida
    template_name = 'ui-cocina.edu.2.delete.html'
    success_url = reverse_lazy('comida_list_1')

class ComidaDeleteView4(DeleteView):
    model = Comida
    template_name = 'ui-cocina.edu.2.delete.html'
    success_url = reverse_lazy('comida_list_1')

class ComidaDeleteView5(DeleteView):
    model = Comida
    template_name = 'ui-cocina.edu.2.delete.html'
    success_url = reverse_lazy('comida_list_1')

class ComidaDeleteView6(DeleteView):
    model = Comida
    template_name = 'ui-cocina.edu.2.delete.html'
    success_url = reverse_lazy('comida_list_1')

class ComidaDeleteView7(DeleteView):
    model = Comida
    template_name = 'ui-cocina.edu.2.delete.html'
    success_url = reverse_lazy('comida_list_1')

class ComidaDeleteView8(DeleteView):
    model = Comida
    template_name = 'ui-cocina.edu.2.delete.html'
    success_url = reverse_lazy('comida_list_1')

class ComidaDeleteView9(DeleteView):
    model = Comida
    template_name = 'ui-cocina.edu.2.delete.html'
    success_url = reverse_lazy('comida_list_1')

class ComidaDeleteView10(DeleteView):
    model = Comida
    template_name = 'ui-cocina.edu.2.delete.html'
    success_url = reverse_lazy('comida_list_1')

class ComidaDeleteView11(DeleteView):
    model = Comida
    template_name = 'ui-cocina.edu.2.delete.html'
    success_url = reverse_lazy('comida_list_1')

#postre
class PostreDeleteView1(DeleteView):
    model = Postre
    template_name = 'ui-cocina.edu.2.delete.html'
    success_url = reverse_lazy('comida_list_1')

class PostreDeleteView2(DeleteView):
    model = Postre
    template_name = 'ui-cocina.edu.2.delete.html'
    success_url = reverse_lazy('comida_list_1')

class PostreDeleteView3(DeleteView):
    model = Postre
    template_name = 'ui-cocina.edu.2.delete.html'
    success_url = reverse_lazy('comida_list_1')

class PostreDeleteView4(DeleteView):
    model = Postre
    template_name = 'ui-cocina.edu.2.delete.html'
    success_url = reverse_lazy('comida_list_1')

class PostreDeleteView5(DeleteView):
    model = Postre
    template_name = 'ui-cocina.edu.2.delete.html'
    success_url = reverse_lazy('comida_list_1')

class PostreDeleteView6(DeleteView):
    model = Postre
    template_name = 'ui-cocina.edu.2.delete.html'
    success_url = reverse_lazy('comida_list_1')

class PostreDeleteView7(DeleteView):
    model = Postre
    template_name = 'ui-cocina.edu.2.delete.html'
    success_url = reverse_lazy('comida_list_1')

class PostreDeleteView8(DeleteView):
    model = Postre
    template_name = 'ui-cocina.edu.2.delete.html'
    success_url = reverse_lazy('comida_list_1')

class PostreDeleteView9(DeleteView):
    model = Postre
    template_name = 'ui-cocina.edu.2.delete.html'
    success_url = reverse_lazy('comida_list_1')

class PostreDeleteView10(DeleteView):
    model = Postre
    template_name = 'ui-cocina.edu.2.delete.html'
    success_url = reverse_lazy('comida_list_1')

class PostreDeleteView11(DeleteView):
    model = Postre
    template_name = 'ui-cocina.edu.2.delete.html'
    success_url = reverse_lazy('comida_list_1')

