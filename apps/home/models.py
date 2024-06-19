# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from .opciones import *
from django.utils import timezone

class Ticket(models.Model):

    titulo = models.CharField(max_length=100)
    urgencia = models.CharField(max_length=10, choices=URGENCIA_CHOICES)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default= 'Abierto')
    creado_por = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField()
    anotaciones = models.TextField(null= True, default= '')

    def __str__(self):
        formatted_fecha = self.fecha.strftime("%d/%m/%Y %H:%M") if self.fecha else "N/A"
        return f"Titulo: {self.titulo} - Urgencia: {self.urgencia} - Fecha: {formatted_fecha}"


class Almacen(models.Model):
    referencia = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=100, choices=TIPO_ALMACEN_CHOICES)
    proveedor = models.CharField(max_length=100)
    modelo = models.CharField(max_length=50)
    cantidad = models.IntegerField(default=0)
    estado = models.CharField(max_length=20,  choices=ESTADO_USO_CHOICES, default='Nuevo')
    descripcion = models.TextField(blank=True, null=True)  
   

    def __str__(self):
        return f"{self.tipo} - {self.modelo} ({self.proveedor})"


class RegistroEvento(models.Model):
    evento = models.CharField(max_length=50)
    fecha_hora = models.DateTimeField(default=timezone.now)


class Inventario(models.Model):
    codigo = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=100, choices=TIPO_CHOICES)
    especificaciones = models.TextField()
    puesto = models.CharField(max_length=100, blank=True, null=True)
    usuario = models.CharField(max_length=100)
    estado = models.CharField(max_length=20, choices=ESTADO_USO_CHOICES, default='Nuevo')
    activo = models.CharField(max_length=20, choices=SI_NO, default='No')

    def __str__(self):
        return f"{self.codigo} - {self.tipo} - {self.puesto} - {self.usuario}"



class Incidencias(models.Model):
    codigo_incidencia = models.AutoField(primary_key=True)
    tipo = models.ForeignKey('Inventario', on_delete=models.CASCADE, related_name='incidencias_tipo')
    texto_incidencia = models.TextField()

    def __str__(self):
        return f"Incidencia #{self.codigo_incidencia} - {self.tipo}"
