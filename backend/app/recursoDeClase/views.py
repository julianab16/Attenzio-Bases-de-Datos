from django.shortcuts import render, redirect
from .serializer import EstudianteClaseForm

def registrarEstudianteClase(request):
    if request.method == 'POST':
        form = EstudianteClaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EstudianteClaseForm()
    return render(request, 'estudianteClase/create_estudiante_clase.html', {'form': form})