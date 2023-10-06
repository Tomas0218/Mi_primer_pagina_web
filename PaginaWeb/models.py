from django.db import models

# Create your models here.
class Curso(models.Model):
    usuario = models.CharField(max_length=50)
    email = models.TextField(max_length=50)
    contrasenia = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.usuario}{self.email}{self.contrasenia}"