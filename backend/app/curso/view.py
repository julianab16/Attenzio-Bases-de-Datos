from rest_framework import generics, status
from rest_framework.response import Response

from .models import Curso
from .forms import CursoForm
from django.shortcuts import render

#def Curso(request): curso_form = CursoForm() return render(request,'curso/curso.html' {'form:curso_form'})