from rest_framework.routers import DefaultRouter
from core.authenticator.api.viewsets import todo_viewsets

# Create a router and register our viewsets with it.
router = DefaultRouter()

router.register(r'register', todo_viewsets.RegisterViewSet, basename='register')
router.register(r'login', todo_viewsets.LoginViewSet, basename='login')
router.register(r'logout', todo_viewsets.LogoutViewSet, basename='logout')
router.register(r'password-reset', todo_viewsets.PasswordResetViewSet, basename='password-reset')
router.register(r'password-reset-confirm', todo_viewsets.PasswordResetConfirmViewSet, basename='password-reset-confirm')
router.register(r'check-session', todo_viewsets.CheckSessionViewSet, basename='check-session')