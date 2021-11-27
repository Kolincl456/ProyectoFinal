from django.db import models
from django.utils import timezone


class Carreras(models.Model):
    nombre  =   models.CharField(max_length=150)

    def __str__(self):
        return self.nombre

class Area(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(
            default=timezone.now)
    fecha_publicacion = models.DateTimeField(
            blank=True, null=True)

    def publicar(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    #def __str__(self):
    ##    return self.title

class Elementos(models.Model):
    nombre  =   models.CharField(max_length=150)

    def __str__(self):
        return self.nombre

class Sector(models.Model):
    
    nombre = models.CharField(max_length=200)

    def publicar(self):
        self.save()


    def __str__(self):
        return self.nombre

    class Meta:
            verbose_name_plural='Sectores'
