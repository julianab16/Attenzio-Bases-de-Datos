from rest_framework import generics, status
from rest_framework.response import Response

from .models import Clase
from django.shortcuts import render, redirect
from .forms import ClaseForm

# Create your views here.

from .serializer import ClaseSerializer


def home(request):
    if request.method == 'POST':
        form = ClaseForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo estudiante en la base de datos
            return redirect('lista_estudiantes')  # Redirige a una página de éxito
    else:
        form = ClaseForm()
        return render(request, 'clase/home.html',  {'form': form})
