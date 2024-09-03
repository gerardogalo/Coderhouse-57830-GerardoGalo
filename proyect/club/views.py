from django.shortcuts import render, redirect
from .models import Socio, Deporte, Instalacion
from .forms import SocioForm, DeporteForm, InstalacionForm

# Create your views here.
def index(request):
    return render(request, "club/index.html")


def socio_list(request):
    query = Socio.objects.all()
    apellido = request.GET.get('apellido')
    estado = request.GET.get('estado')

    if apellido:
        query = query.filter(apellido__icontains=apellido)
    if estado != '' and estado is not None:
        query = query.filter(activo=estado == '1')

    context = {"object_list": query}
    return render(request, "club/socio_list.html", context)

def deporte_list(request):
    query = Deporte.objects.all()
    context = {"object_list": query}
    return render(request, "club/deporte_list.html", context)

def instalaciones_list(request):
    query = Instalacion.objects.all()
    context = {"object_list": query}
    return render(request, "club/instalaciones_list.html", context)

def socio_create(request):
    if request.method == "GET":
        form = SocioForm()
    if request.method == "POST":
        form = SocioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("socio_list")
    return render(request, "club/socio_create.html",{"form": form})

def deporte_create(request):
    if request.method == "GET":
        form = DeporteForm()
    if request.method == "POST":
        form = DeporteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("deporte_list")
    return render(request, "club/deporte_create.html",{"form": form})

def instalaciones_create(request):
    if request.method == "GET":
        form = InstalacionForm()
    if request.method == "POST":
        form = InstalacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("instalaciones_list")
    return render(request, "club/instalaciones_create.html",{"form": form})