# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include 
from apps.home import views
from apps.home.views import *
from django.views.generic.base import TemplateView


urlpatterns = [
   
    path("", include("apps.authentication.urls")), 
    path("", include("apps.home.urls")),            
   
]
