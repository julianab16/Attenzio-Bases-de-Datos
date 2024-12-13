from rest_framework import serializers
from .models import RecursoDeClase

class RecursoDeClaseSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = RecursoDeClase
    fields = '__all__'