from django.shortcuts import render, redirect
from .forms import ProfessorForm, EstudianteForm, ProfessorFormLongin, EstudianteFormLongin


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
            form.save()  # Guarda el objeto en la base de datos
            return redirect('persona_exito')  
    else:
        form = EstudianteForm()

    return render(request, 'usuario/singUpStudent.html', {'form': form})

def loginProfessor(request):
    if request.method == 'POST':
        form = ProfessorFormLongin(request.POST)
        if form.is_valid():
            form.save()  # Guarda el objeto en la base de datos
            return redirect('persona_exito')  
    else:
        form = ProfessorFormLongin()

    return render(request, 'usuario/loginProfessor.html', {'form': form})

def loginStudent(request):
    if request.method == 'POST':
        form = EstudianteFormLongin(request.POST)
        if form.is_valid():
            form.save()  # Guarda el objeto en la base de datos
            return redirect('persona_exito')  
    else:
        form = EstudianteFormLongin()

    return render(request, 'usuario/loginStudents.html', {'form': form})