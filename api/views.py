from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse


class UserViewSet(viewsets.ViewSet):

    def list(self, request):
        # Obtém todos os objetos User do banco de dados
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
        #Retorna uma lista de todos os objetos User no banco de dados.
        #:param request: Requisição HTTP
        #:return: Resposta HTTP com a lista de objetos User

# Método para criar um novo objeto User no banco de dados
    def create(self, request):
        serializer = UserSerializer(data=request.data) # Serializa os objetos User para JSON
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) # Retorna a lista de objetos User com status 200 OK
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)# Obtém o objeto User do banco de dados pelo seu ID
            serializer = UserSerializer(user) # Serializa o objeto User para JSON
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)