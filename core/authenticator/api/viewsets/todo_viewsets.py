from rest_framework import status, viewsets
from core.authenticator.api.serializers.todo_serializers import *
from django.contrib.auth import get_user_model

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from django.contrib.auth import logout, login
from django.contrib.sessions.models import Session
from django.middleware.csrf import get_token
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.conf import settings
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from rest_framework.decorators import action
import threading

# Crear un candado global para bloquear el acceso a la tabla de usuarios
user_update_lock = threading.Lock()


User = get_user_model()

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    authentication_classes = [SessionAuthentication]
    serializer_class = UserSerializer
    queryset = User.objects.all()

class RegisterViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    authentication_classes = [SessionAuthentication]
    serializer_class = RegisterSerializer
    queryset = User.objects.all()



class LoginViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    serializer_class = LoginSerializer
    queryset = User.objects.none()

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data

        # Log in the user
        login(request, user)

        # NOTA: no es necesario obtener y enviar el valor de sessionid
        sessionid = request.session.session_key if request.session.session_key else None

        response = Response({ 
            'status': 'success', 
            'code': status.HTTP_200_OK, 
            "message": "Login successful", 
            'data': { 
                'sessionid': sessionid,
                'csrftoken': get_token(request)
            } 
        })

        response.set_cookie('csrftoken', get_token(request))

        # if sessionid:
        response.set_cookie(key='sessionid', value=sessionid)

        return response

class LogoutViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]
    serializer_class = LogoutSerializer
    queryset = User.objects.none()

    def create(self, request):
        try:
            if not request.user.is_authenticated:
                raise Exception('User already logged out')
                
            logout(request)
            response = Response(data={'success': True, 'message': 'Session closed successfully'})
            response.delete_cookie('sessionid')

            return response

        except Exception as e:
            response = Response(data={'success': False, 'message': str(e)})
        
        return response

class PasswordResetViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = PasswordResetSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data.get('email')
        user = User.objects.filter(email=email).first()

        if user:
            pk_base64 = urlsafe_base64_encode(force_bytes(user.pk))
            user_token = default_token_generator.make_token(user)
            
            # Generate and send password reset email
            subject = 'Password reset on example.com'
            message = 'Please visit the following link to reset your password: ' + request.build_absolute_uri("/api-authenticator/password-reset-confirm/" + pk_base64 + '/' + user_token + '/')
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [user.email]
            send_mail(subject, message, from_email, recipient_list)

            return Response({'message': 'Password reset email sent'}, status=status.HTTP_200_OK)

        return Response({'message': 'User with this email does not exists'}, status=status.HTTP_400_BAD_REQUEST)

class PasswordResetConfirmViewSet(viewsets.ModelViewSet):
    serializer_class = PasswordResetConfirmSerializer
    queryset = User.objects.all()

    def create(self, request, pk_base64, user_token):
        try:
            uid = force_str(urlsafe_base64_decode(pk_base64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, user_token):
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)  # agregar esta línea
            serializer.update(user, serializer.validated_data)
        
            return Response({'detail': 'Password reset successful'}, status=status.HTTP_200_OK)

        return Response({'detail': 'Invalid reset link'}, status=status.HTTP_400_BAD_REQUEST)

class CheckSessionViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    serializer_class = CheckSessionSerializer
    queryset = User.objects.none()

    def retrieve(self, request):
        sessionid = request.COOKIES.get('sessionid', None)
        if sessionid:
            try:
                session = Session.objects.get(session_key=sessionid)
                uid = session.get_decoded().get('_auth_user_id', None)
                if uid:
                    return Response({ 
                        'status': 'success', 
                        'code': status.HTTP_200_OK, 
                        "message": "Session active", 
                    })
            except Session.DoesNotExist:
                pass
        return Response({ 
            'status': 'fail', 
            'code': status.HTTP_401_UNAUTHORIZED, 
            "message": "Session inactive", 
        })

