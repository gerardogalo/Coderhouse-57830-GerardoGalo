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
    SocioListView, SocioCreateView, SocioDetailView,
    DeporteListView, DeporteCreateView, DeporteDetailView,
    InstalacionListView, InstalacionCreateView, InstalacionDetailView,
    SocioUpdateView, DeporteUpdateView, InstalacionUpdateView,
    SocioDeleteView, DeporteDeleteView, InstalacionDeleteView,
    Register, Profile
)
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),  # Asegúrate de que esta línea esté presente
    path('', index, name='index'),
    path('socios/', SocioListView.as_view(), name='socio_list'),
    path('socios/create/', SocioCreateView.as_view(), name='socio_create'),
    path('deportes/', DeporteListView.as_view(), name='deporte_list'),
    path('deportes/create/', DeporteCreateView.as_view(), name='deporte_create'),
    path('instalaciones/', InstalacionListView.as_view(), name='instalaciones_list'),
    path('instalaciones/create/', InstalacionCreateView.as_view(), name='instalaciones_create'),
    path('socios/<int:pk>/', SocioDetailView.as_view(), name='socio_detail'),
    path('deportes/<int:pk>/', DeporteDetailView.as_view(), name='deporte_detail'),
    path('instalaciones/<int:pk>/', InstalacionDetailView.as_view(), name='instalaciones_detail'),
    path('socios/edit/<int:pk>/', SocioUpdateView.as_view(), name='socio_edit'),
    path('deportes/edit/<int:pk>/', DeporteUpdateView.as_view(), name='deporte_edit'),
    path('instalaciones/edit/<int:pk>/', InstalacionUpdateView.as_view(), name='instalaciones_edit'),
    path('socios/delete/<int:pk>/', SocioDeleteView.as_view(), name='socio_delete'),
    path('deportes/delete/<int:pk>/', DeporteDeleteView.as_view(), name='deporte_delete'),
    path('instalaciones/delete/<int:pk>/', InstalacionDeleteView.as_view(), name='instalaciones_delete'),
    path('login/', LoginView.as_view(template_name='club/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='club/logout.html'), name='logout'),
    path('register/', Register.as_view(), name='register'),
    path('profile/', Profile.as_view(), name='profile'),
]

