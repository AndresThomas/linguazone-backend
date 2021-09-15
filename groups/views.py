from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from groups.serializer import GroupSerializer
from groups.models import Group

class Registergroup(APIView): #jerarquia de herencia
    def post(self, request, format = None):
        print(request.data,' registegroup line 11')
        serializer = GroupSerializer(data = request.data)
        print(serializer.is_valid())
        print(request.data, '**********')
        if serializer.is_valid():
            group = serializer.save()
            datas = serializer.data
            return Response(datas, status= status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    

    def get(self, request, format = None):        
        queryset = Group.objects.all()
        serializer = GroupSerializer(queryset, many = True)    
        return Response(serializer.data)


class GroupsList(APIView):
    def get_object(self,id):
        try:
            return Group.objects.get(pk = id)
        except Group.DoesNotExist:
            return 404
    
    def get(self, request, id ,format = None):
        example_object = self.get_object(id) 
        if example_object != 404:
            print('ih')
            serializer = GroupSerializer(example_object)
            return Response(serializer.data)
        return Response("No hay datos")
    
    def put(self,request,id,format = None):
        modify = self.get_object(id)
        print(modify)
        if modify != 404:
            serializer = GroupSerializer(instance= modify, data=request.data)
            print(serializer.is_valid(),' ******')
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                print(datas)
                return Response(datas)
            else:
                print(serializer.errors)
                print(serializer.data)
                return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Este elemento no existe")

    def delete(self, request, id, format=None):
        group = self.get_object(id)
        if group != 404:
            group.delete()
            return Response('Elemento borrado', status=status.HTTP_200_OK)
        else:
            return Response(group, status=status.HTTP_404_NOT_FOUND)