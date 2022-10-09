from rest_framework.routers import DefaultRouter
from core.todo.api.viewsets import todo_viewsets

# Create a router and register our viewsets with it.
router = DefaultRouter()

router.register(r'snippets', todo_viewsets.SnippetViewSet, basename="snippet")
router.register(r'users', todo_viewsets.UserViewSet, basename="user")
router.register(r'todos', todo_viewsets.TodoViewSet, basename="todo")