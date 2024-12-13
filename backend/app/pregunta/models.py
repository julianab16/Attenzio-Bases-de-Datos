from django.db import models
from app.clase.models import Clase
from django.db.models import CASCADE 

class Pregunta(models.Model): 
    clase_id = models.ForeignKey(Clase, null=False, on_delete=models.CASCADE)
    QR = models.IntegerField(primary_key=True, null=False)
    enunciado = models.CharField(null=False, max_length=100)

    class Meta:
        db_table = "pregunta"
        
    def __str__(self):
        return self.name