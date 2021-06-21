from rest_framework import serializers
from Accounts.models import User

class UserSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField()
    email    = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField()
    phone_number = serializers.CharField()
    rol = serializers.CharField()
    
    def create(self, validate_data):
        instance = User()
        instance.username = validate_data.get('username')
        instance.email = validate_data.get('email')
        instance.first_name = validate_data.get('first_name')
        instance.last_name = validate_data.get('last_name')
        instance.role = validate_data.get('rol')
        instance.set_password(validate_data.get('password'))
        instance.set_phone_number = '0000000000'
        instance.save()
        return instance
    
    def validate_username(self, data):
        users = User.objects.filter(username = data)

        if len(users) != 0:
            raise serializers.ValidationError("Este usuario ya esta registrado")
        else:
            return data
    class Meta:
        model = User
        fields = ('__all__')