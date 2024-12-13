from rest_framework import serializers
from .models import EstudianteClase

class EstudianteClaseSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = EstudianteClase
    fields = '__all__'