# CODE TO https://www.django-rest-framework.org/tutorial/quickstart/
""" from core.todo.models import Todo
from rest_framework import viewsets, permissions
from core.todo.api.serializers.todo_serializers import TodoSerializer

# Create your views here.

class TodoViewSet(viewsets.ModelViewSet):
    
    IsAuthenticatedOrReadOnly -> Está autenticado o es de solo lectura \n
    IsAuthenticated -> Está autenticado \n
    AllowAny -> Permitir Cualquiera

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] # [permissions.IsAuthenticatedOrReadOnly] """



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



# CODE TO 
# from core.todo.models import Snippet
# from core.todo.api.serializers.todo_serializers import SnippetSerializer, UserSerializer
# from rest_framework import generics, permissions
# from django.contrib.auth.models import User

# from core.todo.api.permissions.todo_permissions import IsOwnerOrReadOnly
# from rest_framework.reverse import reverse


# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.reverse import reverse
# from rest_framework import renderers

# class SnippetList(generics.ListCreateAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)


# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
#     # IsOwnerOrReadOnly -> Es propietario o solo lectura

#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'users': reverse('user-list', request=request, format=format),
#         'snippets': reverse('snippet-list', request=request, format=format)
#     })

# class SnippetHighlight(generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     renderer_classes = [renderers.StaticHTMLRenderer]

#     def get(self, request, *args, **kwargs):
#         snippet = self.get_object()
#         return Response(snippet.highlighted)





# CODE TO https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/#refactoring-to-use-viewsets
from django.contrib.auth.models import User
from rest_framework import permissions, renderers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from core.todo.models import Snippet, Todo
from core.todo.api.permissions.todo_permissions import IsOwnerOrReadOnly
from core.todo.api.serializers.todo_serializers import SnippetSerializer, UserSerializer, TodoSerializer

from core.todo.api.filters.todo_filters import IsOwnerFilterBackend, IsOwnerFilterBackendUsers

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [IsOwnerFilterBackendUsers]

class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly] # Si no esta auntentificado, solo puede ver los datos, Si el detalle de los datos no los creo el usuario auntentificado solo podra verlos
    filter_backends = [IsOwnerFilterBackend] # filtra solo los datos creador por el usuario autentificado

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TodoViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly] # Si no esta auntentificado, solo puede ver los datos, Si el detalle de los datos no los creo el usuario auntentificado solo podra verlos
    filter_backends = [IsOwnerFilterBackend] # filtra solo los datos creador por el usuario autentificado

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)