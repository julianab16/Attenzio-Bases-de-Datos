from django.db import models

class Curso(models.Model):
    curso_id = models.IntegerField(primary_key=True, blank=True, null=True)
    nombre = models.CharField(max_length=80)
    codigo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)


    class Meta:
        db_table = "curso"
        
    def __str__(self):
        return self.name