from django.db import models
from app.pregunta.models import Pregunta

class Opcion(models.Model):
    OQR = models.IntegerField(primary_key=True, null=False)
    QR = models.ForeignKey(Pregunta, null=False)
    contenido = models.CharField(null=False, max_length=100)
    
    class Meta:
        db_table = "Opcion"
        
    def __str__(self):
        return self.name