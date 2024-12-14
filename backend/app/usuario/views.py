from django.shortcuts import render, redirect
from .forms import ProfessorForm, EstudianteForm


def singUpProfessor(request):
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el objeto en la base de datos
            return redirect('persona_exito')  
    else:
        form = ProfessorForm()

    return render(request, 'usuario/singUpProfessor.html', {'form': form})

def singUpStudent(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            # Si la foto fue cargada, se asigna como datos binarios
            if form.cleaned_data.get('foto'):
                usuario.foto = form.cleaned_data.get('foto')
            usuario.save()
            return redirect('success_url') 
    else:
        form = EstudianteForm()

    return render(request, 'usuario/singUpProfessor.html', {'form': form})