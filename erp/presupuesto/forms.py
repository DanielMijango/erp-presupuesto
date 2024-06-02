# forms.py
from django.forms import ModelForm
from django import forms
from .models import Presupuesto
from .models import Costo

class PresupuestoForm(ModelForm):
    class Meta:
          model = Presupuesto
          fields = ['fecha_inicio', 'nombre', 'descripcion', 'fecha_limite']
          widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_limite': forms.DateInput(attrs={'type': 'date'}),
        }
          

class CostoForm(ModelForm):
    class Meta:
         model = Costo
         fields = ['monto']