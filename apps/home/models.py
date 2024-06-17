# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from .opciones import *

from django.utils import timezone

class Comida(models.Model):
    fecha = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    id_carrito = models.IntegerField()
    tipo_comida = models.CharField(max_length=100, choices=TIPO_GENERAL)
    dieta_aler_otro = models.CharField(max_length=100, choices=TIPO_DIE_ALER)
    sal = models.BooleanField(choices=((False, 'No'), (True, 'Sí')))
    observaciones = models.TextField(blank=True)
    cantidad = models.IntegerField()

    def __str__(self):
        formatted_fecha = self.fecha.strftime("%d/%m/%Y %H:%M") if self.fecha else "N/A"
        return f"Comida - ID Carrito: {self.id_carrito}, Tipo: {self.tipo_comida}, Fecha: {formatted_fecha}"

class Postre(models.Model):
    
    fecha = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    id_carrito = models.IntegerField()
    tipo_postre = models.CharField(max_length=100, choices=TIPO_POSTRE)
    cantidad = models.IntegerField(default=0)

    def __str__(self):
        formatted_fecha = self.fecha.strftime("%d/%m/%Y %H:%M") if self.fecha else "N/A"
        return f"{self.tipo_postre} ID Carrito: {self.id_carrito}, - Cantidad: {self.cantidad}, Fecha: {formatted_fecha}"
