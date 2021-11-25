from django import forms
from .models import Carreras


class CarreraForm(forms.ModelForm):
    class Meta:
        model = Carreras
        fields = ('nombre',)