from django.urls import path
from .import views

urlpatterns = [
    path('carrera/listar', views.carreras_lista, name ='carreras_lista'),
    path('carrera/nueva/', views.carrera_nueva, name='carrera_nueva'),
    path('carrera/<int:pk>/editar/', views.carrera_editar, name ='carrera_editar'),
    path('carrera/<int:pk>', views.carrera_detalle, name ='carrera_detalle'),
    path('carrera/<pk>/borrar/', views.carrera_borrar, name ='carrera_borrar'),
    path('', views.menu, name ='menu'),
    path('area/listar', views.area_lista, name ='area_lista'),
    path('area/<int:pk>', views.area_detalle, name ='area_detalle'),
    path('area/nueva/', views.area_nueva, name='area_nueva'),
    path('area/<int:pk>/editar/', views.area_editar, name ='area_editar'),
    path('area/<pk>/borrar/', views.area_borrar, name ='area_borrar'),
    path('elementos/listar', views.elementos_lista, name ='elementos_lista'),
    path('elementos/nueva/', views.elementos_nueva, name='elementos_nueva'),
    path('elementos/<int:pk>/editar/', views.elementos_editar, name ='elementos_editar'),
    path('elementos/<int:pk>', views.elementos_detalle, name ='elementos_detalle'),
    path('elementos/<pk>/borrar/', views.elementos_borrar, name ='elementos_borrar'),
    path('sector/listar', views.sectores, name='sectores'),
    path('sector/nuevo', views.sector_nuevo, name='sector_nuevo'),
    path('sector/<int:pk>/detalle', views.sector_detalle, name='sector_detalle'),
    path('sector/<int:pk>/editar', views.sector_editar,name='sector_editar'),
    path('sector/<pk>/publicar/',views.sector_publicar,name='sector_publicar'),
    path('sector/<pk>/borrar/', views.sector_borrar, name='sector_borrar'),
    ]