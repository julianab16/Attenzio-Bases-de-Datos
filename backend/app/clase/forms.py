from django import forms
from .models import Clase

class ClaseForm(forms.ModelForm):
    class Meta:
        model = Clase
        fields = ['clase_id', 'curso_id', 'nombre']  # Campos a incluir en el formulario
        # Si deseas excluir algún campo, puedes usar 'exclude' en lugar de 'fields'.
        # exclude = ['edad']