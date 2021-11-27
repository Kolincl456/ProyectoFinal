from django.contrib import messages
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render
from .forms import CarreraForm, AreaForm, ElementoForm, SectorForm
from .models import Carreras, Area, Elementos,Sector
from django.contrib.auth.decorators import login_required


@login_required
def menu(request):
    return render(request,'modulos/menu.html', )
@login_required   
def area_lista(request):
    publicaciones = Area.objects.all()
    return render(request,'modulos/area_lista.html', {'publicaciones': publicaciones})
@login_required
def area_detalle(request,pk):
    publicacion = get_object_or_404(Area, pk = pk)
    return render(request,'modulos/area_detalle.html', {'publicacion': publicacion})
@login_required
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
@login_required
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
@login_required
def area_borrar(request,pk):
    publicacion = get_object_or_404(Area, pk=pk)
    publicacion.delete()
    publicaciones = Area.objects.all()
    return render(request,'modulos/area_lista.html', {'publicaciones': publicaciones})
@login_required
def carreras_lista(request):
    publicaciones = Carreras.objects.all()
    return render(request,'modulos/carreras_lista.html', {'publicaciones': publicaciones})
@login_required
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
@login_required
def carrera_detalle(request,pk):
    publicacion = get_object_or_404(Carreras, pk = pk)
    return render(request,'modulos/carrera_detalle.html', {'publicacion': publicacion})
@login_required
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
@login_required
def carrera_borrar(request,pk):
    publicacion = get_object_or_404(Carreras, pk=pk)
    publicacion.delete()
    publicaciones = Carreras.objects.all()
    return render(request,'modulos/carreras_lista.html', {'publicaciones': publicaciones})
@login_required
def elementos_lista(request):
    publicaciones = Elementos.objects.all()
    return render(request,'modulos/elementos_lista.html', {'publicaciones': publicaciones})
@login_required
def elementos_nueva(request):
    if request.method == "POST":
        formulario = ElementoForm(request.POST)
        if formulario.is_valid():
            publicacion = formulario.save(commit=False)
            publicacion.save()
            messages.add_message(request, messages.SUCCESS, 'Elemento Guardada Exitosamente')
            publicaciones = Elementos.objects.all()
            return render(request,'modulos/elementos_lista.html', {'publicaciones': publicaciones})
    else:
         formulario = ElementoForm()
    return render(request,'modulos/elementos_nueva.html', {'formulario': formulario})
@login_required
def elementos_detalle(request,pk):
    publicacion = get_object_or_404(Elementos, pk = pk)
    return render(request,'modulos/elementos_detalle.html', {'publicacion': publicacion})
@login_required
def elementos_editar(request,pk):
    publicaciones = get_object_or_404(Elementos, pk = pk)
    if request.method =="POST":
        formulario = ElementoForm(request.POST, instance=publicaciones)
        if formulario.is_valid():
            publicaciones = formulario.save(commit=False)
            publicaciones.save()
            publicaciones = Elementos.objects.all()
            publicaciones = Elementos.objects.all()
            return render(request,'modulos/elementos_lista.html', {'publicaciones': publicaciones})
    else:
        formulario = ElementoForm(instance=publicaciones)
    
    return render(request,'modulos/elementos_editar.html', {'formulario': formulario})
@login_required
def elementos_borrar(request,pk):
    publicacion = get_object_or_404(Elementos, pk=pk)
    publicacion.delete()
    publicaciones = Elementos.objects.all()
    return render(request,'modulos/elementos_lista.html', {'publicaciones': publicaciones})

@login_required
def sectores(request):
    sectores= Sector.objects.all()
    return render(request, 'modulos/sectores.html', {'sectores':sectores})
@login_required
def sector_detalle(request,pk):
    sector= get_object_or_404(Sector, pk=pk)
    return render(request, 'modulos/sector_detalle.html', {'sector':sector})

@login_required
def sector_nuevo(request):
    if request.method == "POST":
        formulario = SectorForm(request.POST)
        if formulario.is_valid():
            sector = formulario.save(commit=False)
            sector.save()
            return redirect('sectores',)
    else:
        formulario = SectorForm()
    return render(request, 'modulos/sector_editar.html', {'formulario': formulario})
# Create your views here.

@login_required
def sector_editar(request, pk):
    sector = get_object_or_404(Sector, pk=pk)
    if request.method == "POST":
        formulario = SectorForm(request.POST, instance=sector)
        if formulario.is_valid():
            sector = formulario.save(commit=False)
            sector.save()
            return redirect('sectores')
    else:
        formulario = SectorForm(instance=sector)
    return render(request, 'modulos/sector_editar.html', {'formulario': formulario})

@login_required
def sector_publicar(request,pk):
    sector= get_object_or_404(Sector, pk=pk)
    sector.publicar()
    return redirect('sector_detalle', pk=pk)
    
@login_required
def sector_borrar(request, pk):
    sector= get_object_or_404(Sector, pk=pk)
    sector.delete()
    return redirect('sectores')