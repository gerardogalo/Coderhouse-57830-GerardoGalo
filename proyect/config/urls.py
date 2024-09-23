"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
#from club import views
from django.contrib import admin
from django.urls import path
from club.views import (
    index,
    SocioListView, SocioCreateView,
    DeporteListView, DeporteCreateView,
    InstalacionListView, InstalacionCreateView
)


urlpatterns = [
    path('admin/', admin.site.urls),  # Asegúrate de que esta línea esté presente
    path('', index, name='index'),
    path('socios/', SocioListView.as_view(), name='socio_list'),
    path('socios/create/', SocioCreateView.as_view(), name='socio_create'),
    path('deportes/', DeporteListView.as_view(), name='deporte_list'),
    path('deportes/create/', DeporteCreateView.as_view(), name='deporte_create'),
    path('instalaciones/', InstalacionListView.as_view(), name='instalaciones_list'),
    path('instalaciones/create/', InstalacionCreateView.as_view(), name='instalaciones_create'),
]

