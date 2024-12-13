from rest_framework import generics, status
from rest_framework.response import Response

from .models import Clase
from django.shortcuts import render

# Create your views here.

from .serializer import ClaseSerializer


def home(request):
    contexto = {'mensaje': 'Bienvenida, Julia'}
    return render(request, 'clase/home.html', contexto)
