# CODE TO https://www.django-rest-framework.org/tutorial/quickstart/
from rest_framework import routers
from core.todo.api.viewsets  import todo_viewsets

router = routers.DefaultRouter()
router.register(r'todo', todo_viewsets.TodoViewSet)

urlpatterns = router.urls



""" # CODE TO https://www.youtube.com/watch?v=GE0Q8YNKNgs
from rest_framework import routers
from core.todo.api.viewsets.todo_viewsets  import *

router = routers.DefaultRouter()

router.register('api/todos', TodoViewSet, 'todos')

urlpatterns = router.urls """



""" # CODE TO https://gitlab.com/wdavilav/apolo/-/blob/master/core/api/urls.py
from django.urls import path
from core.todo.api.viewsets.todo_viewsets  import *
from core.todo.api.routers import router

urlpatterns = [
    path('todo/', TodoAPIView.as_view(), name='api_todo'),
    path('todo/list/', TodoListAPIView.as_view(), name='api_todo_list'),
    path('todo/create/', TodoCreateAPIView.as_view(), name='api_todo_create'),
    path('todo/update/<int:pk>/', TodoUpdateAPIView.as_view(), name='api_todo_update'),
    path('todo/delete/<int:pk>/', TodoDestroyAPIView.as_view(), name='api_todo_delete'),
]

urlpatterns += router.urls """
