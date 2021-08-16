from languages.models import Language
from rest_framework import serializers

class LanguageSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    language = serializers.CharField()
    teacher = serializers.CharField()
    level = serializers.CharField()
    link = serializers.CharField()
    usn = serializers.CharField()
    
    def create(self, validate_data):
        instance = Language()
        instance.language = validate_data.get('language')
        instance.teacher = validate_data.get('teacher')
        instance.level = validate_data.get('level')
        instance.link = validate_data.get('link')
        instance.usn = validate_data.get('usn')
        instance.save()
        return instance
    
    class Meta:
        model = Language
        fields = ('__all__')