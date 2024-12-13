from django.db import models
from app.clase.models import Clase

class RecursoDeClase(models.Model):
    rid = models.IntegerField(primary_key=True, null=False)
    clase_id = models.ForeignKey(Clase, null=False, on_delete=models.CASCADE)
    url = models.CharField(max_length=300, null=False)
    
    class Meta:
        db_table = "RecursoDeClase"
        
    def __str__(self):
        return self.name