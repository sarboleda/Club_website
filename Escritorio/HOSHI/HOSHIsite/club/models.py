from django.db import models
from django.utils import timezone

class Inscrip(models.Model):
    DNI = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    Nombre = models.CharField(max_length=100)
    text = models.TextField()
    Inicio_date = models.DateTimeField(
        default=timezone.now)

def __str__(self):
    return self.title

