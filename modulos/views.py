from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .forms import CarreraForm
from .models import Carreras

def area_lista(request):
    return render(request,'modulos/area_lista.html',) 
