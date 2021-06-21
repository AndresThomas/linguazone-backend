from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Register.serializer import UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from Accounts.models import User

class RegisterUser(ObtainAuthToken,APIView): #jerarquia de herencia
    def post(self, request, format = None):
        print(request.data,' registeuser line 11')
        serializer = UserSerializer(data = request.data)
        print(serializer.is_valid())
        
        if serializer.is_valid():
            user = serializer.save()
            datas = serializer.data
            token,created = Token.objects.get_or_create(user=user)            
            
            return Response(datas, status= status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    

    def get(self, request, format = None):
        print("Get in register")
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many = True)
        return Response(serializer.data)