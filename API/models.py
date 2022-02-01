import uuid
from django.db import models


# Create your models here.
class Usuario(models.Model):
    ID = models.UUIDField(
        primary_key=True,
        unique=True,
        default=uuid.uuid4,
        )
    Nombre = models.TextField(max_length=200)
    Apellido = models.TextField(max_length=200)
    Email = models.EmailField(max_length=200, unique=True)
    FechaNac = models.DateField()

    class Meta:
        ordering = ['ID']

    def __str__(self):
        return self.Nombre + ' ' + self.Apellido + ' ' + self.Email
