""" # CODE TO https://gitlab.com/wdavilav/apolo/-/blob/master/core/api/routers.py
from rest_framework.routers import DefaultRouter

from core.todo.api.viewsets.todo_viewsets import TodoViewSet

router = DefaultRouter()
router.register(r'todo', TodoViewSet, basename='todo')
 """