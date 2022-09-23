# CODE TO https://www.django-rest-framework.org/tutorial/quickstart/
from core.todo.models import Todo
from rest_framework import viewsets, permissions
from core.todo.api.serializers.todo_serializers import TodoSerializer
from core.todo.api.permissions.todo_permissions import IsOwnerOrReadOnly

# Create your views here.

class TodoViewSet(viewsets.ModelViewSet):
    """
    IsAuthenticatedOrReadOnly -> Está autenticado o es de solo lectura \n
    IsAuthenticated -> Está autenticado \n
    AllowAny -> Permitir Cualquiera
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly] # [permissions.IsAuthenticatedOrReadOnly]



""" # CODE TO https://www.youtube.com/watch?v=GE0Q8YNKNgs AND https://www.digitalocean.com/community/tutorials/build-a-to-do-application-using-django-and-react
from rest_framework import viewsets, permissions
from core.todo.api.serializers.todo_serializers import TodoSerializer
from core.todo.models import Todo

# Create your views here.

class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    permission_classes = [permissions.AllowAny] # [permissions.IsAuthenticated]
    queryset = Todo.objects.all() """



""" # CODE TO https://gitlab.com/wdavilav/apolo/-/blob/master/core/api/views.py
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from core.todo.api.serializers.todo_serializers import TodoSerializers
from core.todo.models import Todo

class TodoAPIView(APIView):
    def get(self, request, *args, **kwargs):
        print(self.request.query_params)
        return Response({'resp': False})

    def post(self, request, *args, **kwargs):
        queryset = Todo.objects.all()
        serializer = [i.toJSON() for i in queryset]
        return Response(serializer)

class TodoListAPIView(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print(self.queryset)
        serializer = self.serializer_class(self.queryset.all(), many=True)
        return Response(serializer.data)
    
class TodoCreateAPIView(CreateAPIView):
    serializer_class = TodoSerializers

    def post(self, request, *args, **kwargs):
        print(self.request.data)
        return self.create(request, *args, **kwargs)

class TodoUpdateAPIView(UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers

    def put(self, request, *args, **kwargs):
        print(self.request.data)
        return self.update(request, *args, **kwargs)

class TodoDestroyAPIView(DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers

    def delete(self, request, *args, **kwargs):
        instance = self.queryset.get(pk=self.kwargs['pk'])
        instance.delete()
        return Response({'msg': f"Se ha eliminado correctamente el pk {self.kwargs['pk']}"})

class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers

    def list(self, request, *args, **kwargs):
        return Response({'id': 4}) """
