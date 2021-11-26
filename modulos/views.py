from django.contrib import messages
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render
from .forms import CarreraForm, AreaForm
from .models import Carreras, Area

def menu(request):
    return render(request,'modulos/menu.html', )
    
def area_lista(request):
    publicaciones = Area.objects.all()
    return render(request,'modulos/area_lista.html', {'publicaciones': publicaciones})

def area_detalle(request,pk):
    publicacion = get_object_or_404(Area, pk = pk)
    return render(request,'modulos/area_detalle.html', {'publicacion': publicacion})

def area_nueva(request):
    if request.method == "POST":
        formulario = AreaForm(request.POST)
        if formulario.is_valid():
            publicacion = formulario.save(commit=False)
            publicacion.autor = request.user
            publicacion.fecha_publicacion = timezone.now()
            publicacion.fecha_creacion = timezone.now()
            publicacion.save()
            messages.add_message(request, messages.SUCCESS, 'Area Guardada Exitosamente')
            publicaciones = Area.objects.all()
            return render(request,'modulos/area_lista.html', {'publicaciones': publicaciones})
    else:
         formulario = AreaForm()
    return render(request,'modulos/area_nueva.html', {'formulario': formulario})

def area_editar(request,pk):
    publicaciones = get_object_or_404(Area, pk = pk)
    if request.method =="POST":
        formulario = AreaForm(request.POST, instance=publicaciones)
        if formulario.is_valid():
            publicaciones = formulario.save(commit=False)
            publicaciones.autor = request.user
            publicaciones.fecha_publicacion = timezone.now()
            publicaciones.fecha_creacion = timezone.now()
            publicaciones.save()
            publicaciones = Area.objects.all()
            return render(request,'modulos/area_lista.html', {'publicaciones': publicaciones})
    else:
        formulario = AreaForm(instance=publicaciones)
    return render(request,'modulos/area_editar.html', {'formulario': formulario})

def area_borrar(request,pk):
    publicacion = get_object_or_404(Area, pk=pk)
    publicacion.delete()
    publicaciones = Area.objects.all()
    return render(request,'modulos/area_lista.html', {'publicaciones': publicaciones})

def carreras_lista(request):
    publicaciones = Carreras.objects.all()
    return render(request,'modulos/carreras_lista.html', {'publicaciones': publicaciones})

def carrera_nueva(request):
    if request.method == "POST":
        formulario = CarreraForm(request.POST)
        if formulario.is_valid():
            publicacion = formulario.save(commit=False)
            publicacion.save()
            messages.add_message(request, messages.SUCCESS, 'Carrera Guardada Exitosamente')
            publicaciones = Carreras.objects.all()
            return render(request,'modulos/carreras_lista.html', {'publicaciones': publicaciones})
    else:
         formulario = CarreraForm()
    return render(request,'modulos/carrera_nueva.html', {'formulario': formulario})

def carrera_detalle(request,pk):
    publicacion = get_object_or_404(Carreras, pk = pk)
    return render(request,'modulos/carrera_detalle.html', {'publicacion': publicacion})

def carrera_editar(request,pk):
    publicaciones = get_object_or_404(Carreras, pk = pk)
    if request.method =="POST":
        formulario = CarreraForm(request.POST, instance=publicaciones)
        if formulario.is_valid():
            publicaciones = formulario.save(commit=False)
            publicaciones.save()
            publicaciones = Carreras.objects.all()
            return render(request,'modulos/carreras_lista.html', {'publicaciones': publicaciones})
    else:
        formulario = CarreraForm(instance=publicaciones)
    
    return render(request,'modulos/carrera_editar.html', {'formulario': formulario})

def carrera_borrar(request,pk):
    publicacion = get_object_or_404(Carreras, pk=pk)
    publicacion.delete()
    publicaciones = Carreras.objects.all()
    return render(request,'modulos/carreras_lista.html', {'publicaciones': publicaciones})
