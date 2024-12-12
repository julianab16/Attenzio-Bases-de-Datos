from django.db import models
from app.clase.models import Clase

class Pregunta(models.Model): 
    clase_id = models.ForeignKey(Clase, null=False)
    QR = models.IntegerField(primary_key=True, null=False)
    enunciado = models.CharField(null=False, max_length=100)

    class Meta:
        db_table = "Pregunta"
        
    def __str__(self):
        return self.name