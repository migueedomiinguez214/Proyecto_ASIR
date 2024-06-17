# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.contrib import admin
from django.urls import path, re_path
from apps.home import views
from apps.home.views import *
from django.views.generic.base import TemplateView

urlpatterns = [
    
    # The home page
    path('', views.index, name='home'),
    path('user/', views.page_user, name='page_user'),
    
    path('educacion/', views.educacion, name='educacion'),
    path('educacion/ciclo1/carro1/', Comida1CreateView.as_view(), name='crear_carrito1'),
    path('educacion/ciclo1/carro2/', Comida2CreateView.as_view(), name='crear_carrito2'),
    path('educacion/ciclo2/carro3/', Comida3CreateView.as_view(), name='crear_carrito3'),
    path('educacion/ciclo3/carro4/', Comida4CreateView.as_view(), name='crear_carrito4'),
    path('educacion/ciclo3/carro5/', Comida5CreateView.as_view(), name='crear_carrito5'),
    path('educacion/PTVAL/carro6/', Comida6CreateView.as_view(), name='crear_carrito6'),
    path('educacion/ciclo1/carro1/postre/', Postre1CreateView.as_view(), name='crear_postre1'),
    path('educacion/ciclo1/carro2/postre/', Postre2CreateView.as_view(), name='crear_postre2'),
    path('educacion/ciclo2/carro3/postre/', Postre3CreateView.as_view(), name='crear_postre3'),
    path('educacion/ciclo3/carro4/postre/', Postre4CreateView.as_view(), name='crear_postre4'),
    path('educacion/ciclo3/carro5/postre/', Postre5CreateView.as_view(), name='crear_postre5'),
    path('educacion/PTVAL/carro6/postre/', Postre6CreateView.as_view(), name='crear_postre6'),

    path('residencia/', views.residencias, name='residencia'),
    path('residencia/AllAndalus/carro7/', Comida7CreateView.as_view(), name='crear_carrito7'),
    path('residencia/RGA/carro8/', Comida8CreateView.as_view(), name='crear_carrito8'),
    path('residencia/AllAndalus/carro7/postre/', Postre7CreateView.as_view(), name='crear_postre7'),
    path('residencia/RGA/carro8/postre/', Postre8CreateView.as_view(), name='crear_postre8'),

    path('ocupacional/', views.ocupacional, name='ocupacional'),
    path('ocupacional/carro9/', Comida9CreateView.as_view(), name='crear_carrito9'),
    path('ocupacional/carro9/postre/', Postre9CreateView.as_view(), name='crear_postre9'),

    path('unidaddia/', views.unidaddia, name='unidaddia'),
    path('unidaddia/comedor1/carro10/', Comida10CreateView.as_view(), name='crear_carrito10'),
    path('unidaddia/comedor2/carro11/', Comida11CreateView.as_view(), name='crear_carrito11'),
    path('unidaddia/comedor1/carro10/postre/', Postre10CreateView.as_view(), name='crear_postre10'),
    path('unidaddia/comedor2/carro11/postre/', Postre11CreateView.as_view(), name='crear_postre11'),

    path('cocina/', views.cocina, name='cocina'),
    path('cocina/educacion/', views.cocinaedu, name='cocinaedu'),
    path('cocina/residencia/', views.cocinaresi, name='cocinaresi'),
    path('cocina/ocupacional/', views.cocinaocu, name='cocinaocu'),
    path('cocina/unidaddia/', views.cocinaunid, name='cocinaunid'),

    path('cocina/educacion/comida/1/', ComidaListView1.as_view(), name='comida_list_1'),
    path('cocina/educacion/comida/2/', ComidaListView2.as_view(), name='comida_list_2'),
    path('cocina/educacion/comida/3/', ComidaListView3.as_view(), name='comida_list_3'),
    path('cocina/educacion/comida/4/', ComidaListView4.as_view(), name='comida_list_4'),
    path('cocina/educacion/comida/5/', ComidaListView5.as_view(), name='comida_list_5'),
    path('cocina/educacion/comida/6/', ComidaListView6.as_view(), name='comida_list_6'),
    path('cocina/residencia/comida/7/', ComidaListView7.as_view(), name='comida_list_7'),
    path('cocina/residencia/comida/8/', ComidaListView8.as_view(), name='comida_list_8'),
    path('cocina/ocupacional/comida/9/', ComidaListView9.as_view(), name='comida_list_9'),
    path('cocina/unidaddia/comida/10/', ComidaListView10.as_view(), name='comida_list_10'),
    path('cocina/unidaddia/comida/11/', ComidaListView11.as_view(), name='comida_list_11'),

    path('cocina/educacion/comida/1/<int:pk>/editar/', ComidaUpdateView1.as_view(), name='comida_update_1'),
    path('cocina/educacion/comida/2/<int:pk>/editar/', ComidaUpdateView2.as_view(), name='comida_update_2'),
    path('cocina/educacion/comida/3/<int:pk>/editar/', ComidaUpdateView3.as_view(), name='comida_update_3'),
    path('cocina/educacion/comida/4/<int:pk>/editar/', ComidaUpdateView4.as_view(), name='comida_update_4'),
    path('cocina/educacion/comida/5/<int:pk>/editar/', ComidaUpdateView5.as_view(), name='comida_update_5'),
    path('cocina/educacion/comida/6/<int:pk>/editar/', ComidaUpdateView6.as_view(), name='comida_update_6'),
    path('cocina/educacion/comida/7/<int:pk>/editar/', ComidaUpdateView7.as_view(), name='comida_update_7'),
    path('cocina/educacion/comida/8/<int:pk>/editar/', ComidaUpdateView8.as_view(), name='comida_update_8'),
    path('cocina/educacion/comida/9/<int:pk>/editar/', ComidaUpdateView9.as_view(), name='comida_update_9'),
    path('cocina/educacion/comida/10/<int:pk>/editar/', ComidaUpdateView10.as_view(), name='comida_update_10'),
    path('cocina/educacion/comida/1/1<int:pk>/editar/', ComidaUpdateView11.as_view(), name='comida_update_11'),

    path('cocina/educacion/comida/1/postre/<int:pk>/editar/', PostreUpdateView1.as_view(), name='postre_update_1'),
    path('cocina/educacion/comida/2/postre/<int:pk>/editar/', PostreUpdateView2.as_view(), name='postre_update_2'),
    path('cocina/educacion/comida/3/postre/<int:pk>/editar/', PostreUpdateView3.as_view(), name='postre_update_3'),
    path('cocina/educacion/comida/4/postre/<int:pk>/editar/', PostreUpdateView4.as_view(), name='postre_update_4'),
    path('cocina/educacion/comida/5/postre/<int:pk>/editar/', PostreUpdateView5.as_view(), name='postre_update_5'),
    path('cocina/educacion/comida/6/postre/<int:pk>/editar/', PostreUpdateView6.as_view(), name='postre_update_6'),
    path('cocina/educacion/comida/7/postre/<int:pk>/editar/', PostreUpdateView7.as_view(), name='postre_update_7'),
    path('cocina/educacion/comida/8/postre/<int:pk>/editar/', PostreUpdateView8.as_view(), name='postre_update_8'),
    path('cocina/educacion/comida/9/postre/<int:pk>/editar/', PostreUpdateView9.as_view(), name='postre_update_9'),
    path('cocina/educacion/comida/10/postre/<int:pk>/editar/', PostreUpdateView10.as_view(), name='postre_update_10'),
    path('cocina/educacion/comida/11/postre/<int:pk>/editar/', PostreUpdateView11.as_view(), name='postre_update_11'),

    path('cocina/educacion/comida/1/<int:pk>/borrar/', ComidaDeleteView1.as_view(), name='comida_borrar_1'),
    path('cocina/educacion/comida/2/<int:pk>/borrar/', ComidaDeleteView2.as_view(), name='comida_borrar_2'),
    path('cocina/educacion/comida/3/<int:pk>/borrar/', ComidaDeleteView3.as_view(), name='comida_borrar_3'),
    path('cocina/educacion/comida/4/<int:pk>/borrar/', ComidaDeleteView4.as_view(), name='comida_borrar_4'),
    path('cocina/educacion/comida/5/<int:pk>/borrar/', ComidaDeleteView5.as_view(), name='comida_borrar_5'),
    path('cocina/educacion/comida/6/<int:pk>/borrar/', ComidaDeleteView6.as_view(), name='comida_borrar_6'),
    path('cocina/educacion/comida/7/<int:pk>/borrar/', ComidaDeleteView7.as_view(), name='comida_borrar_7'),
    path('cocina/educacion/comida/8/<int:pk>/borrar/', ComidaDeleteView8.as_view(), name='comida_borrar_8'),
    path('cocina/educacion/comida/9/<int:pk>/borrar/', ComidaDeleteView9.as_view(), name='comida_borrar_9'),
    path('cocina/educacion/comida/10/<int:pk>/borrar/', ComidaDeleteView10.as_view(), name='comida_borrar_10'),
    path('cocina/educacion/comida/11/<int:pk>/borrar/', ComidaDeleteView11.as_view(), name='comida_borrar_11'),
    
    path('cocina/educacion/comida/1/postre/<int:pk>/borrar/', PostreDeleteView1.as_view(), name='postre_borrar_1'),
    path('cocina/educacion/comida/2/postre/<int:pk>/borrar/', PostreDeleteView2.as_view(), name='postre_borrar_2'),
    path('cocina/educacion/comida/3/postre/<int:pk>/borrar/', PostreDeleteView3.as_view(), name='postre_borrar_3'),
    path('cocina/educacion/comida/4/postre/<int:pk>/borrar/', PostreDeleteView4.as_view(), name='postre_borrar_4'),
    path('cocina/educacion/comida/5/postre/<int:pk>/borrar/', PostreDeleteView5.as_view(), name='postre_borrar_5'),
    path('cocina/educacion/comida/6/postre/<int:pk>/borrar/', PostreDeleteView6.as_view(), name='postre_borrar_6'),
    path('cocina/educacion/comida/7/postre/<int:pk>/borrar/', PostreDeleteView7.as_view(), name='postre_borrar_7'),
    path('cocina/educacion/comida/8/postre/<int:pk>/borrar/', PostreDeleteView8.as_view(), name='postre_borrar_8'),
    path('cocina/educacion/comida/9/postre/<int:pk>/borrar/', PostreDeleteView9.as_view(), name='postre_borrar_9'),
    path('cocina/educacion/comida/10/postre/<int:pk>/borrar/', PostreDeleteView10.as_view(), name='postre_borrar_10'),
    path('cocina/educacion/comida/11/postre/<int:pk>/borrar/', PostreDeleteView11.as_view(), name='postre_borrar_11'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

    path('panel-admin/', admin.site.urls),
 
]
