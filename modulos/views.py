from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .forms import CarreraForm
from .models import Carreras

def menu(request):
    return render(request,'modulos/menu.html', )
    
def area_lista(request):
    return render(request,'modulos/area_lista.html',) 
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
