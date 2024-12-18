from django import forms
from .models import Usuario
import re

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['correo', 'contraseña', 'nombre', 'id', 'direccion']
    
    
    def clean_correo(self):
        correo = self.cleaned_data['correo']
        # Verificar que el correo tenga un formato válido
        if not re.match(r"[^@]+@[^@]+\.[^@]+", correo):
            raise forms.ValidationError("Por favor, ingresa un correo válido.")
        return correo

    def clean_id(self):
        user_id = self.cleaned_data['id']
        # Asegúrate de que el ID no se repita
        if Usuario.objects.filter(id=user_id).exists():
            raise forms.ValidationError("Este ID ya está registrado.")
        return user_id


class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['correo', 'contraseña', 'nombre', 'numeroCelular', 'direccion']
    
    def clean_numeroCelular(self):
        numero_celular = self.cleaned_data['numeroCelular']
        # Verificar que el número de celular no contenga letras
        # Verificar que el número de celular no sea None
        if numero_celular and not numero_celular.isdigit():
            raise forms.ValidationError("El número de celular debe contener solo números.")
    
        # Si es None o vacío, se puede devolver None o un valor predeterminado
        return numero_celular

    def clean_correo(self):
        correo = self.cleaned_data['correo']
        # Verificar que el correo tenga un formato válido
        if not re.match(r"[^@]+@[^@]+\.[^@]+", correo):
            raise forms.ValidationError("Por favor, ingresa un correo válido.")
        return correo
    

class ProfessorFormLongin(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['correo', 'contraseña']
    
    
    def clean_correo(self):
        correo = self.cleaned_data['correo']
        # Verificar que el correo tenga un formato válido
        if not re.match(r"[^@]+@[^@]+\.[^@]+", correo):
            raise forms.ValidationError("Por favor, ingresa un correo válido.")
        return correo

class EstudianteFormLongin(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['correo', 'contraseña']

    def clean_correo(self):
        correo = self.cleaned_data['correo']
        # Verificar que el correo tenga un formato válido
        if not re.match(r"[^@]+@[^@]+\.[^@]+", correo):
            raise forms.ValidationError("Por favor, ingresa un correo válido.")
        return correo