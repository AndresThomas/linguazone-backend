from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from languages.serializer import LanguageSerializer
from languages.models import Language
# Create your views here.
class LanguageList(APIView):
    def get_object(self,id):
        try:
            return Language.objects.get(pk = id)
        except Language.DoesNotExist:
            return 404
    def get(self, request, id ,format = None):
        example_object = self.get_object(id) 
        if example_object != 404:
            serializer = LanguageSerializer(example_object)
            return Response(serializer.data)
        return Response("No hay datos")

    def delete(self, request, id, format=None):
        user = self.get_object(id)
        if user != 404:
            user.delete()
            return Response('Elemento borrado', status=status.HTTP_200_OK)
        else:
            return Response(user, status=status.HTTP_404_NOT_FOUND)

    def put(self,request,id,format = None):
        modify = self.get_object(id)

        if modify != 404:
            serializer = LanguageSerializer(modify, data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas)
            else:
                print(serializer.error)
                return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Este elemento no existe")

    


class RegisterLanguage(APIView):
    def post(self, request, format = None):
        print(request.data,' registeuser line 11')
        serializer = LanguageSerializer(data = request.data)
        print(serializer.is_valid())
        
        if serializer.is_valid():
            language = serializer.save()
            datas = serializer.data
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
            serializer = LanguageSerializer(queryset, many = True)
        elif( request.query_params.get('rol') == 'student'):
            print('teachers')
            queryset = Language.objects.all().filter(rol='teacher')
            serializer = LanguageSerializer(queryset, many = True)
        else:
            queryset = Language.objects.all()
            serializer = LanguageSerializer(queryset, many = True)    
        return Response(serializer.data)