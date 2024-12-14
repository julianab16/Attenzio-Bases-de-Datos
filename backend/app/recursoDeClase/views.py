from django.shortcuts import render, redirect, get_object_or_404
from .models import RecursoDeClase, Clase
from .forms import RecursoDeClaseForm

def create_recurso(request, clase_id):
    clase = get_object_or_404(Clase, id=clase_id)
    
    if request.method == 'POST':
        form = RecursoDeClaseForm(request.POST)
        if form.is_valid():
            recurso = form.save(commit=False)
            recurso.clase_id = clase
            recurso.save()
            return redirect('success')
    else:
        form = RecursoDeClaseForm()
    
    return render(request, 'create_recurso.html', {'form': form, 'clase': clase})

def success(request):
    return render(request, 'success.html')