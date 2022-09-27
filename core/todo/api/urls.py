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



# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from rest_framework.urlpatterns import format_suffix_patterns
# from core.todo.api.viewsets import todo_viewsets

# from core.todo.api.viewsets import todo_viewsets, SnippetViewSet, UserViewSet, api_root
# from rest_framework import renderers

""" urlpatterns = [
    path('snippets/', todo_viewsets.SnippetList.as_view(), name='snippet-list'),
    path('snippets/<int:pk>/', todo_viewsets.SnippetDetail.as_view()),
    path('users/', todo_viewsets.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', todo_viewsets.UserDetail.as_view()),


    path('', todo_viewsets.api_root),
    path('snippets/<int:pk>/highlight/', todo_viewsets.SnippetHighlight.as_view()),
] """



# API endpoints
""" urlpatterns = [
    path('', todo_viewsets.api_root),

    path('snippets/', todo_viewsets.SnippetList.as_view(), name='snippet-list'),
    path('snippets/<int:pk>/', todo_viewsets.SnippetDetail.as_view(), name='snippet-detail'),
    path('snippets/<int:pk>/highlight/', todo_viewsets.SnippetHighlight.as_view(), name='snippet-highlight'),
    
    path('users/', todo_viewsets.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', todo_viewsets.UserDetail.as_view(), name='user-detail')
] """



""" snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    path('', api_root),

    path('snippets/', snippet_list, name='snippet-list'),
    path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
    path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail')
] """

# urlpatterns = format_suffix_patterns(urlpatterns)





from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.todo.api.viewsets import todo_viewsets

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', todo_viewsets.SnippetViewSet,basename="snippet")
router.register(r'users', todo_viewsets.UserViewSet,basename="user")
router.register(r'todos', todo_viewsets.TodoViewSet,basename="todo")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]