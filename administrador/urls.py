"""web_admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django import views  # <<==========
from administrador import views  # <<==========


urlpatterns = [
    path('home/', views.index, name="home"),  # <<==========

    path('newhome', views.home, name="homenew"),
    path('homecafe/', views.cafe, name="homecafe"),
    path('agregar/', views.agregar, name="agregar"),
    path('eliminar/', views.eliminar, name="eliminar"),
    path('editar/', views.editar, name="editar"),

    # path('eliminar/<int:cafe_id>/', views.eliminar, name="eliminar"),
    # path('editar/<int:cafe_id>/', views.editar, name="editar"),
    path('pruebas/', views.pruebas, name="pruebas"),
    path('ejemplos/', views.ejemplos, name="ejemplos"),

    path('ddavimo/', views.ddavimo, name="ddavimo"),


    # ***********************************************************************

    # Ventas

    path('ventas/', views.ventas, name="ventas"),

    # Geeks

    path('geeks/', views.index, name="index"),
    path('geeks/create', views.create_view, name="create"),
    path('geeks/list', views.list_view, name="list"),
    path('geeks/detail/<int:id>', views.detail_view, name="detail"),
    path('geeks/update', views.update_view, name="update"),
    path('geeks/delete/<int:id>', views.delete_view, name="delete"),
    path('geeks/calc', views.calc, name="calc"),




]
