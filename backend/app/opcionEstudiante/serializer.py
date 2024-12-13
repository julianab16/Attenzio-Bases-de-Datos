from rest_framework import serializers
from .models import OpcionEstudiante

class OpcionEstudianteSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = OpcionEstudiante
    fields = '__all__'