from django import forms
from .models import Carreras, Area, Elementos, Sector

class CarreraForm(forms.ModelForm):
    class Meta:
        model = Carreras
        fields = ('nombre',)

class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ('titulo', 'nombre', 'descripcion', )
    
class ElementoForm(forms.ModelForm):
    class Meta:
        model = Elementos
        fields = ('nombre',)

class SectorForm(forms.ModelForm):
    class Meta:
        model= Sector
        fields=('nombre',)