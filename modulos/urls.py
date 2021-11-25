from django.urls import path
from .import views

urlpatterns = [
    path('', views.menu, name ='menu'),
    path('carrera/listar', views.carreras_lista, name ='carreras_lista'),
    path('area/listar', views.area_lista, name ='area_lista'),
    path('carrera/nueva/', views.carrera_nueva, name='carrera_nueva'),
    path('carrera/<int:pk>/editar/', views.carrera_editar, name ='carrera_editar'),
    path('carrera/<int:pk>', views.carrera_detalle, name ='carrera_detalle'),
    path('carrera/<pk>/borrar/', views.carrera_borrar, name ='carrera_borrar'),
    ]