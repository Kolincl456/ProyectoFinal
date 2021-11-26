from django.urls import path
from .import views

urlpatterns = [
    path('', views.menu, name ='menu'),
    path('area/listar', views.area_lista, name ='area_lista'),
    path('area/<int:pk>', views.area_detalle, name ='area_detalle'),
    path('area/nueva/', views.area_nueva, name='area_nueva'),
    path('area/<int:pk>/editar/', views.area_editar, name ='area_editar'),
    path('area/<pk>/borrar/', views.area_borrar, name ='area_borrar'),
    path('carrera/listar', views.carreras_lista, name ='carreras_lista'),
    path('carrera/nueva/', views.carrera_nueva, name='carrera_nueva'),
    path('carrera/<int:pk>/editar/', views.carrera_editar, name ='carrera_editar'),
    path('carrera/<int:pk>', views.carrera_detalle, name ='carrera_detalle'),
    path('carrera/<pk>/borrar/', views.carrera_borrar, name ='carrera_borrar'),
    ]