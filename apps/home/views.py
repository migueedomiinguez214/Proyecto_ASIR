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
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import get_object_or_404
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
import os
import csv
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    
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


def page_user(request):
    return render(request, 'page-user.html')

def custom_logout_view(request):
    logout(request)
    return redirect('index')  

#PERMISOS-----------------------------------------------------------------

def informatico(user):
    return user.groups.filter(name='informatico').exists()

def almacen(user):
    return user.groups.filter(name='almacen').exists()

def superuser(user):
    return user.groups.filter(name='superuser').exists()

def inventario(user):
    return user.groups.filter(name='inventario').exists()

#TICKETS------------------------------------------------------------------

class TicketCreateView(LoginRequiredMixin, CreateView):
    model = Ticket
    form_class= TicketForm
    template_name = 'ticket_crear.html'
    success_url = reverse_lazy('ticket-list')  

    def form_valid(self, form):
        form.instance.creado_por = self.request.user
        return super().form_valid(form)

"""
class TicketCreateView(LoginRequiredMixin, CreateView):
    model = Ticket
    form_class = TicketForm
    template_name = 'ticket_crear.html'
    success_url = reverse_lazy('ticket-list')  # Cambia 'ticket-list' por el nombre de la URL a la que quieras redirigir después de crear un ticket

    def form_valid(self, form):
        # Asigna el usuario actual como el creador del ticket
        form.instance.creado_por = self.request.user

        # Guarda el ticket
        super().form_valid(form)

        # Envía el correo electrónico
        send_mail(
            'Nuevo Ticket Creado',
            'Se ha creado un nuevo ticket.',
            'tu_correo@dominio.com',  # Cambia 'tu_correo@dominio.com' por tu dirección de correo electrónico
            ['correo_destino@dominio.com'],  # Cambia 'correo_destino@dominio.com' por la dirección de correo a la que quieras enviar el correo
            fail_silently=False,
        )

        return super().form_valid(form)
"""


class TicketListView(LoginRequiredMixin, ListView):
    model = Ticket
    template_name = 'ticket_list.html'
    context_object_name = 'tickets'

    def get_queryset(self):
        user = self.request.user

        # Obtener el estado de la URL
        estado = self.request.GET.get('estado')
        
        if user.is_superuser:
            if estado:
                return Ticket.objects.filter(estado=estado)
            else:
                return Ticket.objects.all()
        else:
            if estado:
                return Ticket.objects.filter(creado_por=user, estado=estado)
            else:
                return Ticket.objects.filter(creado_por=user)

@method_decorator(user_passes_test(informatico), name='dispatch')
class TicketDeleteView(DeleteView):
    model = Ticket
    success_url = reverse_lazy('ticket-list')
    template_name = 'ticket_confirm_delete.html'


class TicketEditView(UserPassesTestMixin, UpdateView):
    model = Ticket
    template_name = 'ticket_edit.html'
    fields = '__all__'  
    success_url = reverse_lazy('ticket-list') 

    def test_func(self):
       
        return self.request.user.groups.filter(name='super').exists()

    def handle_no_permission(self):
        return redirect('ticket-list')  

    def form_valid(self, form):
        if self.request.user.groups.filter(name='super').exists():
            return super().form_valid(form)
        return redirect('ticket-list') 

        
def generar_pdf_ticket(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename=Ticket{pk}_informacion.pdf'

    pdf = SimpleDocTemplate(response, pagesize=letter)

    content = []

    styles = getSampleStyleSheet()
    style_title = styles["Title"]
    style_title.alignment = 1  # Centrar el título
    style_table = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Color de fondo para la cabecera
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),  # Color de texto para la cabecera
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),  # Alinear a la izquierda
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),  # Color de fondo para las filas
        ('GRID', (0, 0), (-1, -1), 0.25, colors.black)  # Líneas de la tabla más finas
    ])

    # Encabezado
    header = Paragraph("ADMINISTRACIÓN DE INFORMÁTICA", style_title)
    content.append(header)
    content.append(Spacer(1, 12))  # Espacio después del encabezado

    # Título del ticket
    title = Paragraph(f"Parte del Ticket - {ticket.titulo}", style_title)
    content.append(title)
    content.append(Spacer(1, 12))  # Espacio después del título

    # Datos del ticket
    ticket_data = [
        ["Título:", ticket.titulo],
        ["Urgencia:", ticket.urgencia],
        ["Estado:", ticket.estado],
        ["Creado Por:", ticket.creado_por.username],
        ["Fecha:", ticket.fecha.strftime('%d/%m/%Y %H:%M')],
        ["Descripción:", ticket.descripcion],
        ["Anotaciones:", ticket.anotaciones if ticket.anotaciones else "N/A"]
    ]

    tabla = Table(ticket_data, colWidths=[100, 400])  # Ancho de las columnas ajustado
    tabla.setStyle(style_table)
    content.append(tabla)

    content.append(Spacer(1, 24))  # Espacio después de la tabla

    # Información de contacto
    contacto_info = "CONTACTO: 662082011\nmigueedomiinguez@gmail.com"
    style_contacto = styles["Normal"]
    style_contacto.fontSize = 12  # Tamaño de fuente más pequeño para contacto
    content.append(Paragraph(contacto_info, style_contacto))

    pdf.build(content)

    return response


#ALMACEN-------------------------------------------------------------------------------------

@method_decorator(user_passes_test(almacen  ), name='dispatch')
class AlmacenListView(LoginRequiredMixin, ListView):
    model = Almacen
    template_name = 'almacen_list.html'
    context_object_name = 'almacenes'
    ordering = ['tipo']  

    def test_func(self):
        return self.request.user.groups.filter(name='super').exists()

    def get_queryset(self):
        queryset = super().get_queryset()
        tipo = self.request.GET.get('tipo')
        if tipo:
            queryset = queryset.filter(tipo=tipo)
        return queryset

@method_decorator(user_passes_test(almacen  ), name='dispatch')
class AlmacenCreateView(CreateView):
    model = Almacen
    fields= '__all__'
    template_name = 'almacen_create.html'
    success_url = reverse_lazy('almacen_list')

    def form_valid(self, form):
        almacen = form.save(commit=False)
        almacen.save()
        evento = f"Añadido a Almacen: {almacen}"
        RegistroEvento.objects.create(evento=evento)
        return super().form_valid(form)

@method_decorator(user_passes_test(almacen  ), name='dispatch')
class AlmacenEditView(View):
    fields = '__all__'

    def get(self, request, referencia):
        almacen = get_object_or_404(Almacen, referencia=referencia)
        form = AlmacenForm(instance=almacen)
        return render(request, 'almacen_edit.html', {'form': form, 'almacen': almacen})

    def post(self, request, referencia):
        almacen = get_object_or_404(Almacen, referencia=referencia)
        form = AlmacenForm(request.POST, instance=almacen)
        if form.is_valid():
            almacen = form.save()
            evento = f"Editado Almacen: {almacen}"
            RegistroEvento.objects.create(evento=evento)
            return redirect('almacen_list')
        return render(request, 'almacen_edit.html', {'form': form, 'almacen': almacen})

@method_decorator(user_passes_test(almacen  ), name='dispatch')
class AlmacenDeleteView(View):
    fields = '__all__'

    def get(self, request, referencia):
        almacen = get_object_or_404(Almacen, referencia=referencia)
        return render(request, 'almacen_confirm_delete.html', {'almacen': almacen})

    def post(self, request, referencia):
        almacen = get_object_or_404(Almacen, referencia=referencia)
        evento = f"Eliminado de Almacen: {almacen}"
        RegistroEvento.objects.create(evento=evento)
        almacen.delete()
        return redirect('almacen_list')


def generar_pdf_almacenes(request):
    almacenes = Almacen.objects.all()

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="almacenes.pdf"'

    p = canvas.Canvas(response, pagesize=letter)
    
    width, height = letter
    max_rows_per_page = 40
    padding = 20
    x_offset = 50
    y_offset = 50
    padding = 15
    available_height = height - 2 * y_offset
    row_height = 20
    space_between_columns = 150

    titulo = "Lista de Productos de Almacén"
    titulo_width = p.stringWidth(titulo, "Helvetica-Bold", 16)  
    p.setFont("Helvetica-Bold", 16)
    p.drawString((width - titulo_width) / 2, height - 50, titulo)  
    fecha_actual = datetime.now().strftime("%d/%m/%Y")
    p.setFont("Helvetica", 12)
    p.drawString(width // 2 - 40, height - 70, f"Fecha: {fecha_actual}")

    row_y = height - y_offset - padding - 50  
    p.setFont("Helvetica-Bold", 12)
    p.drawString(x_offset, row_y, "Tipo")
    p.drawString(x_offset + space_between_columns, row_y, "Proveedor")
    p.drawString(x_offset + 2 * space_between_columns, row_y, "Modelo")
    p.drawString(x_offset + 3 * space_between_columns, row_y, "Cantidad")
    p.drawString(x_offset + 4 * space_between_columns, row_y, "Estado")
    p.drawString(x_offset + 5 * space_between_columns, row_y, "Descripción")
    row_y -= row_height

    for almacen in almacenes:
        if row_y <= y_offset:
            p.showPage()
            p.setFont("Helvetica-Bold", 12)
            row_y = height - y_offset - padding
            p.drawString(x_offset, row_y, "Tipo")
            p.drawString(x_offset + space_between_columns, row_y, "Proveedor")
            p.drawString(x_offset + 2 * space_between_columns, row_y, "Modelo")
            p.drawString(x_offset + 3 * space_between_columns, row_y, "Cantidad")
            p.drawString(x_offset + 4 * space_between_columns, row_y, "Estado")
            p.drawString(x_offset + 5 * space_between_columns, row_y, "Descripción")
            row_y -= row_height

        p.setFont("Helvetica", 12)
        p.drawString(x_offset, row_y, str(almacen.tipo))
        p.drawString(x_offset + space_between_columns, row_y, str(almacen.proveedor))
        p.drawString(x_offset + 2 * space_between_columns, row_y, str(almacen.modelo))
        p.drawString(x_offset + 3 * space_between_columns, row_y, str(almacen.cantidad))
        p.drawString(x_offset + 4 * space_between_columns, row_y, str(almacen.estado))
        p.drawString(x_offset + 5 * space_between_columns, row_y, str(almacen.descripcion))
        row_y -= row_height

    p.showPage()
    p.save()
    return response

class RegistroEventoListView(ListView):
    model = RegistroEvento
    template_name = 'pagina_registros.html'
    context_object_name = 'registros'
    ordering = ['-fecha_hora']



#USUARIOS-----------------------------------------------------------------------------------------

@method_decorator(user_passes_test(superuser  ), name='dispatch')
class CustomUserCreateView(CreateView):
    model = User
    fields = ['username', 'password', 'first_name', 'last_name','is_superuser', 'is_staff', 'is_active']
    template_name = 'user_create.html'
    success_url = '/user/create/'

@method_decorator(user_passes_test(superuser  ), name='dispatch')
class CustomUserListView(ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'users'

@method_decorator(user_passes_test(superuser  ), name='dispatch')
class CustomUserUpdateView(UpdateView):
    model = User
    fields = ['username', 'password', 'first_name', 'last_name', 'is_superuser', 'is_staff', 'is_active']
    template_name = 'user_update.html'
    success_url = reverse_lazy('list_users')  

@method_decorator(user_passes_test(superuser  ), name='dispatch')
class CustomUserDeleteView(DeleteView):
    model = User
    template_name = 'user_confirm_delete.html'
    success_url = reverse_lazy('list_users') 

def search_users(request):
    query = request.GET.get('search')
    if query:
        users = User.objects.filter(username__icontains=query)
    else:
        users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})


#INVENTARIO----------------------------------------------------------------------------------------

@method_decorator(user_passes_test(inventario  ), name='dispatch')
class InventarioListView(ListView):
    model = Inventario
    template_name = 'inventario_list.html'
    context_object_name = 'inventarios'

@method_decorator(user_passes_test(inventario  ), name='dispatch')
class InventarioCreateView(LoginRequiredMixin, CreateView):
    model = Inventario
    fields = ['tipo', 'especificaciones', 'puesto','usuario', 'estado', 'activo']
    template_name = 'inventario_create.html'
    success_url = reverse_lazy('inventario_list')

    

@method_decorator(user_passes_test(inventario  ), name='dispatch')
class InventarioDeleteView(DeleteView):
    model = Inventario
    template_name = 'inventario_confirm_delete.html'
    success_url = reverse_lazy('inventario_list')

@method_decorator(user_passes_test(inventario  ), name='dispatch')
class InventarioUpdateView(UpdateView):
    model = Inventario
    fields = ['tipo', 'especificaciones', 'puesto', 'usuario', 'estado', 'activo']
    template_name = 'inventario_update.html'
    success_url = reverse_lazy('inventario_list')

@method_decorator(user_passes_test(inventario  ), name='dispatch')
class IncidenciasListView(ListView):
    model = Incidencias
    template_name = 'incidencias_list.html'
    context_object_name = 'incidencias'

@method_decorator(user_passes_test(inventario  ), name='dispatch')
class IncidenciasCreateView(CreateView):
    model = Incidencias
    fields = ['tipo', 'texto_incidencia']
    template_name = 'incidencias_create.html'
    success_url = reverse_lazy('incidencias_list')

@method_decorator(user_passes_test(inventario  ), name='dispatch')
class IncidenciasDeleteView(DeleteView):
    model = Incidencias
    template_name = 'incidencias_confirm_delete.html'
    success_url = reverse_lazy('incidencias_list')

@method_decorator(user_passes_test(inventario  ), name='dispatch')
class IncidenciasUpdateView(UpdateView):
    model = Incidencias
    fields = ['tipo', 'texto_incidencia']
    template_name = 'incidencias_update.html'
    success_url = reverse_lazy('incidencias_list')

@method_decorator(user_passes_test(inventario  ), name='dispatch')
class IncidenciaCreateView(CreateView):
    model = Incidencias
    template_name = 'crear_incidencia.html'
    fields = ['texto_incidencia']

    def form_valid(self, form):
        inventario_id = self.kwargs['inventario_id']
        inventario = Inventario.objects.get(pk=inventario_id)
        form.instance.tipo = inventario
        return super().form_valid(form)

    def get_success_url(self):
        inventario_id = self.kwargs['inventario_id']
        return reverse_lazy('incidencias_list', kwargs={'pk': inventario_id})