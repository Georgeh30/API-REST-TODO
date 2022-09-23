""" from rest_framework.routers import DefaultRouter

from core.todo.api.viewsets.todo_viewsets import TodoViewSet

router = DefaultRouter()
router.register(r'client', TodoViewSet, basename='client')
 """