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
        print("Get in register 27")
        print(request.query_params)
        
        if( request.query_params.get('rol') == 'teacher'):
            print('students')
            queryset = User.objects.all().filter(rol='student')
            serializer = UserSerializer(queryset, many = True)
        elif( request.query_params.get('rol') == 'student'):
            print('teachers')
            queryset = User.objects.all().filter(rol='teacher')
            serializer = UserSerializer(queryset, many = True)
        else:
            queryset = User.objects.all()
            serializer = UserSerializer(queryset, many = True)    
        return Response(serializer.data)


class UsersList(APIView):
    def get_object(self,id):
        try:
            return User.objects.get(pk = id)
        except User.DoesNotExist:
            return 404
    
    def get(self, request, id ,format = None):
        example_object = self.get_object(id) 
        if example_object != 404:
            print('ih')
            serializer = UserSerializer(example_object)
            return Response(serializer.data)
        return Response("No hay datos")
    
    def put(self,request,id,format = None):
        modify = self.get_object(id)
        print(modify,' soy modify')
        if modify != 404:
            serializer = UserSerializer(modify, data=request.data)
            print(serializer.is_valid(), ' is valid?')
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                print(datas)
                return Response(datas)
            else:
                print(request.data) 
                print(serializer.errors)
                return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Este elemento no existe")

    def delete(self, request, id, format=None):
        user = self.get_object(id)
        if user != 404:
            user.delete()
            return Response('Elemento borrado', status=status.HTTP_200_OK)
        else:
            return Response(user, status=status.HTTP_404_NOT_FOUND)