from django import forms
from .models import RecursoDeClase

class RecursoDeClaseForm(forms.ModelForm):
  
  class Meta:
    model = RecursoDeClase
    fields = ['url']