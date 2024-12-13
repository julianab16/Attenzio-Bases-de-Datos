from django.db import models
from app.usuario.models import Usuario
from app.clase.models import Clase
from django.db.models import CASCADE 


class EstudianteClase(models.Model):
    id = models.AutoField(primary_key=True) 
    usuario_id = models.ForeignKey(Usuario, null=False, on_delete=models.CASCADE)
    clase_id = models.ForeignKey(Clase, on_delete=models.CASCADE)
    fecha = models.DateField(null=False)
    hora = models.TimeField(null=False)
    latitud = models.CharField(null=False, max_length=50)
    latitud = models.CharField(null=False, max_length=50)
    
    class Meta:
        db_table = "estudianteClase",
        unique_together = ('usuario_id', 'clase_id') 

        
    def __str__(self):
        return f"{self.usuario_id} - {self.clase_id}"