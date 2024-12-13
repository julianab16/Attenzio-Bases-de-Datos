from django.db import models

class Rol(models.Model):
    rol_id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=80)

    class Meta:
        db_table = "rol"
        
    def __str__(self):
        return self.name