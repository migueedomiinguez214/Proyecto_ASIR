# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin

# Register your models here.

from .models import Comida
admin.site.register(Comida)

from .models import Postre
admin.site.register(Postre)

