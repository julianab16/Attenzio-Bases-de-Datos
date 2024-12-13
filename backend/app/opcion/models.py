from django.db import models
from app.pregunta.models import Pregunta
from django.db.models import CASCADE 

class Opcion(models.Model):
    OQR = models.IntegerField(primary_key=True, null=False)
    QR = models.ForeignKey(Pregunta, null=False, on_delete=models.CASCADE)
    contenido = models.CharField(null=False, max_length=100)
    
    class Meta:
        db_table = "opcion"
        
    def __str__(self):
        return self.name