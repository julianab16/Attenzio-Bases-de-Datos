from django.db import models
from app.usuario.models import Usuario
from app.clase.models import Clase

class EstudianteClase(models.Model):
    id = models.ForeignKey(Usuario, primary_key=True, null=False)
    clase_id = models.ForeignKey(Clase, primary_key=True, null=False)
    fecha = models.DateTimeField(auto_now_add=True, null=False)
#    hora = models.TimeField(null=False)
    latitud = models.CharField(null=False, max_length=50)
    latitud = models.CharField(null=False, max_length=50)
    
    class Meta:
        db_table = "EstudianteClase"
        
    def __str__(self):
        return self.name