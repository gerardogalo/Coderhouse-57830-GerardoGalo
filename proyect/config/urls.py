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
from django.contrib import admin
from django.urls import path
from club import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path("socio/list/", views.socio_list, name="socio_list"),
    path("deporte/list/", views.deporte_list, name="deporte_list"),
    path("instalaciones/list/", views.instalaciones_list, name="instalaciones_list"),
    path("socio/create/", views.socio_create, name="socio_create"),
    path("deporte/create/", views.deporte_create, name="deporte_create"),
    path("instalaciones/create/", views.instalaciones_create, name="instalaciones_create"),
]

