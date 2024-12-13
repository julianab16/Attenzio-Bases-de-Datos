from django.db import models
from app.curso.models import Curso


class Clase(models.Model):
    clase_id = models.IntegerField(primary_key=True, blank=True, null=True)
    curso_id = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=80)
    fecha = models.DateField(null=False)
    hora = models.TimeField(null=False)


    class Meta:
        db_table = "Clase"
        
    def __str__(self):
        return self.name