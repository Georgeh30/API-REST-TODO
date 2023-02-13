# CODE TO https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/#refactoring-to-use-viewsets
from rest_framework import permissions, renderers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from core.todo.models import Snippet, Todo
from core.todo.api.permissions.todo_permissions import IsOwnerOrReadOnly
from core.todo.api.serializers.todo_serializers import SnippetSerializer, UserCreateSerializer, UserSerializer, TodoSerializer # NEW

from core.todo.api.filters.todo_filters import IsOwnerFilterBackend, IsOwnerFilterBackendUsers
from django.contrib.auth import get_user_model # NEW

User = get_user_model() # NEW

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

    IsAuthenticatedOrReadOnly -> Está autenticado o es de solo lectura \n
    IsAuthenticated -> Está autenticado \n
    AllowAny -> Permitir Cualquiera \n
    IsOwnerOrReadOnly -> Si es el creador del objeto, si no solo lectura \n
    IsOwnerFilterBackend -> Se filtrara solo sus objetos creados por el
    """
    queryset = Todo.objects.all() # queryset -> lista de objetos de un modelo determinado
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly] # Si no esta auntentificado, solo puede ver los datos, Si el detalle de los datos no los creo el usuario auntentificado solo podra verlos
    filter_backends = [IsOwnerFilterBackend] # filtra solo los datos creador por el usuario autentificado

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

#  NEW PER CREATING NEW USER
class UserCreateViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    filter_backends = [IsOwnerFilterBackendUsers]

    def perform_create(self, serializer):
        serializer.save()