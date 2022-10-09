from django.urls import path
from core.todo.api.routers import router
from rest_framework.authtoken.views import obtain_auth_token

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'), # Generator token authentication
]

urlpatterns += router.urls