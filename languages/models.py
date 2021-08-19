from django.db import models

# Create your models here.
class Language(models.Model):
    language = models.CharField(max_length=30)
    teacher = models.CharField(max_length=30)
    level = models.CharField(max_length=30)
    link = models.CharField(max_length=100)
    usn = models.CharField(max_length=30)