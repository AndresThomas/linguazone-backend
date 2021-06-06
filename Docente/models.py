from django.db import models

class LanguagesField(models.CharField):
    data =[]

    def __init__(self,*args, **kwargs):
        kwargs['max_length'] = 100000
        super().__init__(*args, **kwargs)


class Alumn(models.Model):
    languages = LanguagesField()


class Teacher(models.Model):
    languages = LanguagesField()
    group_class = models.ManyToManyField(Alumn)

