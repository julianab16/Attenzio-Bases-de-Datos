from django.shortcuts import render

# Create your views here.

from rest_framework import generics, status
from rest_framework.response import Response

from .models import RecursoDeClase
from .serializer import RecursoDeClaseSerializer

class ListCreateRecursoDeClase(generics.ListAPIView):
  queryset = RecursoDeClase.objects.all()
  serializer_class = RecursoDeClaseSerializer
  
  def post(self, request, *args, **kwargs):
    data= request.data
    serr = RecursoDeClaseSerializer(data=data)
    if (serr.is_valid()):
      serr.save()
      return Response(serr.validated_data, status=status.HTTP_200_OK)  
    
    return Response(status=status.HTTP_400_BAD_REQUEST)