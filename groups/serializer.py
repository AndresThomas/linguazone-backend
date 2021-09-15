from django.db import models
from groups.models import Group
from rest_framework import serializers

class GroupSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField()
    teacher = serializers.JSONField()
    link_clases = serializers.CharField()
    lista_alumnos = serializers.JSONField()
    
    
    def create(self, validate_data):
        instance = Group()
        instance.teacher = validate_data.get('teacher')
        instance.name = validate_data.get('name')
        instance.link_clases = validate_data.get('link_clases')
        instance.lista_alumnos = validate_data.get('lista_alumnos')
        
        instance.save()
        return instance
    
    class Meta:
        model = Group
        fields = ('__all__')