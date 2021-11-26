from django import forms
from .models import Carreras, Area

class CarreraForm(forms.ModelForm):
    class Meta:
        model = Carreras
        fields = ('nombre',)

class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ('titulo', 'nombre', 'descripcion', )