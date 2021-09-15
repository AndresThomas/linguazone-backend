from django.db import models

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=30)
    teacher = models.JSONField()
    link_clases = models.CharField(max_length=255)
    lista_alumnos = models.JSONField()

