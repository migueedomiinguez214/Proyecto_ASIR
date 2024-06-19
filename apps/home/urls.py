# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.contrib import admin
from django.urls import path, re_path, include 
from apps.home import views
from apps.home.views import *
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    # The home page
    path('', views.index, name='home'),
    path('user/', views.page_user, name='page_user'),
    path('logout/', custom_logout_view, name='logout'),
    
    #TICKETS------------------------------------------------------

    path('crear-ticket/', TicketCreateView.as_view(), name='crear_ticket'),
    path('tickets/', TicketListView.as_view(), name='ticket-list'),
    path('tickets/<int:pk>/delete/', TicketDeleteView.as_view(), name='ticket_delete'),
    path('tickets/<int:pk>/edit/', TicketEditView.as_view(), name='ticket_edit'),
    path('tickets/<int:pk>/imprimir/', generar_pdf_ticket, name='ticket-imprimir'),


    #ALMACEN------------------------------------------------------
    path('almacen/', AlmacenListView.as_view(), name='almacen_list'),
    path('almacen/<int:referencia>/edit/', AlmacenEditView.as_view(), name='almacen_edit'),
    path('almacen/<int:referencia>/delete/', AlmacenDeleteView.as_view(), name='almacen_delete'),
    path('almacen/pdf/', generar_pdf_almacenes, name='generar_pdf_almacenes'),
    path('almacen-crear/', AlmacenCreateView.as_view(), name='almacen_create'),
    path('registros/', RegistroEventoListView.as_view(), name='registros_eventos'),


    #INVENTARIO--------------------------------------------------

    path('inventario/list/', InventarioListView.as_view(), name='inventario_list'),
    path('inventario/create/', InventarioCreateView.as_view(), name='inventario_create'),
    path('inventario/<int:pk>/delete/', InventarioDeleteView.as_view(), name='inventario_delete'),
    path('inventario/<int:pk>/update/', InventarioUpdateView.as_view(), name='inventario_update'),
    
    
    path('incidencias/list/', IncidenciasListView.as_view(), name='incidencias_list'),
    path('incidencias/create/', IncidenciasCreateView.as_view(), name='incidencias_create'),
    path('incidencias/<int:pk>/delete/', IncidenciasDeleteView.as_view(), name='incidencias_delete'),
    path('incidencias/<int:pk>/update/', IncidenciasUpdateView.as_view(), name='incidencias_update'),

    path('inventario/<int:inventario_id>/incidencia/create/', IncidenciaCreateView.as_view(), name='incidencia_create2'),

    #USUARIOS----------------------------------------------------

    path('user/create/', CustomUserCreateView.as_view(), name='user_create'),
    path('user/list/', CustomUserListView.as_view(), name='user_list'),
    path('user/<int:pk>/edit/', CustomUserUpdateView.as_view(), name='edit_user'),
    path('user/<int:pk>/delete/', CustomUserDeleteView.as_view(), name='delete_user'),
    path('user/search/', search_users, name='search_users'),

    #GENERICAS----------------------------------------------------
    re_path(r'^.*\.*', views.pages, name='pages'),
    path('panel-admin/', admin.site.urls),

   
   
]
