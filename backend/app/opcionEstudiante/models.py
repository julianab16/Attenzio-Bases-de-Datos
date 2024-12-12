from django.db import models
from app.usuario.models import Usuario
from app.pregunta.models import Pregunta


class OpcionEstudiante(models.Model): 
    OQR = models.IntegerField(primary_key=True, null=False)
    id = models.ForeignKey(Usuario, primary_key=True, null=False)
    QR = models.ForeignKey(Pregunta, null=False)
    puntaje = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    latitud = models.CharField(null=False, max_length=50)
    longitud = models.CharField(null=False, max_length=50)

    class Meta:
        db_table = "OpcionEstudiante"
        
    def __str__(self):
        return self.name