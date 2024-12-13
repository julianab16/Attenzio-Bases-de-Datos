from rest_framework import generics, status
from rest_framework.response import Response

from .models import Curso
from django.shortcuts import render

#def Curso(request): curso_form = CursoForm() return render(request,'curso/curso.html' {'form:curso_form'})

# Create your views here.

from .serializer import CursoSerializer

class ListCreateCurso(generics.ListAPIView):
  queryset = Curso.objects.all()
  serializer_class = CursoSerializer
  
  def post(self, request, *args, **kwargs):
    data= request.data
    serr = CursoSerializer(data=data)
    if (serr.is_valid()):
      serr.save()
      return Response(serr.validated_data, status=status.HTTP_200_OK)  
    
    return Response(status=status.HTTP_400_BAD_REQUEST)