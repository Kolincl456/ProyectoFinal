from django import forms
from .models import Carreras, Area, Elementos, Sector

class CarreraForm(forms.ModelForm):
    class Meta:
        model = Carreras
        fields = ('nombre',)

class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ('titul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o', 'nombre', 'descripcion', )
    
class ElementoForm(forms.ModelForm):
    class Meta:
        model = Elementos
        fields = ('nombre',)

class SectorForm(forms.ModelForm):
    class Meta:
        model= Sector
        fields=('nombre',)