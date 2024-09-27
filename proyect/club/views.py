from django.shortcuts import render
from .models import Socio, Deporte, Instalacion
from .forms import SocioForm, DeporteForm, InstalacionForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(request, "club/index.html")

# Lista de socios
class SocioListView(ListView):
    model = Socio
    template_name = 'club/socio_list.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        queryset = Socio.objects.all()
        apellido = self.request.GET.get('apellido')
        estado = self.request.GET.get('estado')

        if apellido:
            queryset = queryset.filter(apellido__icontains=apellido)
        if estado != '' and estado is not None:
            queryset = queryset.filter(activo=estado == '1')

        return queryset

# Lista de deportes
class DeporteListView(ListView):
    model = Deporte
    template_name = 'club/deporte_list.html'
    context_object_name = 'object_list'

# Lista de instalaciones
class InstalacionListView(ListView):
    model = Instalacion
    template_name = 'club/instalaciones_list.html'
    context_object_name = 'object_list'



# Crear socio
class SocioCreateView(CreateView):
    model = Socio
    form_class = SocioForm
    template_name = 'club/socio_form.html'
    success_url = reverse_lazy('socio_list')

# Crear deporte
class DeporteCreateView(CreateView):
    model = Deporte
    form_class = DeporteForm
    template_name = 'club/deporte_form.html'
    success_url = reverse_lazy('deporte_list')

# Crear instalación
class InstalacionCreateView(CreateView):
    model = Instalacion
    form_class = InstalacionForm
    template_name = 'club/instalaciones_form.html'
    success_url = reverse_lazy('instalaciones_list')



# Detalle de socio
class SocioDetailView(DetailView):
    model = Socio
    template_name = 'club/socio_detail.html'

# Detalle de deporte
class DeporteDetailView(DetailView):
    model = Deporte
    template_name = 'club/deporte_detail.html'

# Detalle de instalación
class InstalacionDetailView(DetailView):
    model = Instalacion
    template_name = 'club/instalaciones_detail.html'



# Editar socio
class SocioUpdateView(UpdateView):
    model = Socio
    form_class = SocioForm
    template_name = 'club/socio_form.html'
    success_url = reverse_lazy('socio_list')

# Editar deporte
class DeporteUpdateView(UpdateView):
    model = Deporte
    form_class = DeporteForm
    template_name = 'club/deporte_form.html'
    success_url = reverse_lazy('deporte_list')

# Editar instalación
class InstalacionUpdateView(UpdateView):
    model = Instalacion
    form_class = InstalacionForm
    template_name = 'club/instalaciones_form.html'
    success_url = reverse_lazy('instalaciones_list')