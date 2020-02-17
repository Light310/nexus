"""Nexus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),
    path('', views.index),
    path('view-stream/', views.view_stream),
    path('get_speed', views.get_speed),
    path('set_speed', views.set_speed),
    path('get_batteries_values', views.get_batteries_values),
    path('get_gyroaccel_data', views.get_gyroaccel_data),    
    path('get_fenix_data', views.get_fenix_data),     
    path('command', views.command),
    path('read_command', views.read_command),
]
