# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin

from .models import Ticket
admin.site.register(Ticket)

from .models import Almacen
admin.site.register(Almacen)

from .models import Inventario
admin.site.register(Inventario)

from .models import Incidencias
admin.site.register(Incidencias)

from .models import RegistroEvento
admin.site.register(RegistroEvento)