from django.urls import path
from .import views

urlpatterns = [
    path('', views.area_lista, name='area_lista'),
]
