""" # CODE TO https://www.django-rest-framework.org/tutorial/quickstart/
from rest_framework import routers
from core.todo.api.viewsets  import todo_viewsets

router = routers.DefaultRouter()
router.register(r'todo', todo_viewsets.TodoViewSet)

urlpatterns = router.urls """



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



from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from core.todo.api.viewsets import todo_viewsets

""" urlpatterns = [
    path('snippets/', todo_viewsets.SnippetList.as_view(), name='snippet-list'),
    path('snippets/<int:pk>/', todo_viewsets.SnippetDetail.as_view()),
    path('users/', todo_viewsets.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', todo_viewsets.UserDetail.as_view()),


    path('', todo_viewsets.api_root),
    path('snippets/<int:pk>/highlight/', todo_viewsets.SnippetHighlight.as_view()),
] """

# API endpoints
urlpatterns = [
    path('', todo_viewsets.api_root),

    path('snippets/', todo_viewsets.SnippetList.as_view(), name='snippet-list'),
    path('snippets/<int:pk>/', todo_viewsets.SnippetDetail.as_view(), name='snippet-detail'),
    path('snippets/<int:pk>/highlight/', todo_viewsets.SnippetHighlight.as_view(), name='snippet-highlight'),
    
    path('users/', todo_viewsets.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', todo_viewsets.UserDetail.as_view(), name='user-detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)