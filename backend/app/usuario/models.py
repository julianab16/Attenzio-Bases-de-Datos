from django.db import models
from app.rol.models import Rol
from django.db.models import CASCADE 

class Usuario(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)
    nombre = models.CharField(max_length=80)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    correo = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=50)
    numeroCelular = models.CharField(max_length=50, blank=True, null=True)
    rol_id = models.ForeignKey(Rol, on_delete=models.CASCADE, db_column='rol_id')
    foto = models.BinaryField(blank=True, null=True) 

    class Meta:
        db_table = "usuario"
        
    def __str__(self):
        return self. nombre