from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator

class Contacto(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    telefono = models.PositiveIntegerField(validators=[MaxValueValidator(99999999)])
    fechaRegistro = models.DateField(auto_now_add=timezone.now())
    
    def __str__(self):
        return f"[id: {self.id}] -> {self.nombre} -- {self.apellido} -- {self.telefono}"


