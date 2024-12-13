from django.db import models
from app.usuario.models import Usuario
from app.pregunta.models import Pregunta
from django.db.models import CASCADE 

class OpcionEstudiante(models.Model): 
    OQR = models.IntegerField(primary_key=True)
    id = models.ForeignKey(Usuario, null=False, on_delete=models.CASCADE)
    QR = models.ForeignKey(Pregunta, null=False, on_delete=models.CASCADE)
    puntaje = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    latitud = models.CharField(null=False, max_length=50)
    longitud = models.CharField(null=False, max_length=50)

    class Meta:
        db_table = "opcionEstudiante"
        unique_together = ('QR', 'id') 

        
    def __str__(self):
        return self.name