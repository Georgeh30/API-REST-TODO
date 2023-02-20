from base64 import urlsafe_b64decode
from sqlite3 import IntegrityError
from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from rest_framework import status
from django.contrib.auth.hashers import make_password

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']

class RegisterSerializer(serializers.ModelSerializer):
    confirm_email = serializers.EmailField(write_only=True)
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'confirm_email', 'nick_name', 'username', 'first_name', 'last_name', 'password', 'confirm_password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        email = data.get('email')
        confirm_email = data.get('confirm_email')
        
        if email != confirm_email:
            raise serializers.ValidationError("Emails must match")

        password = data.get('password')
        confirm_password = data.get('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError("Passwords must match")

        validate_password(password)
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            confirm_email=validated_data['confirm_email'],
            nick_name=validated_data['nick_name'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password'],
            is_staff=True
        )

        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active and user.is_staff:
            return user
        raise serializers.ValidationError({
            'status': 'error',
            'code': status.HTTP_401_UNAUTHORIZED,
            'message': 'Username or password incorrect',
            'data': {}
        })

class LogoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = []

class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        user = User.objects.filter(email=value).first()
        if not user:
            raise serializers.ValidationError('User with this email does not exists')
        return value
        
class PasswordResetConfirmSerializer(serializers.Serializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match")
        return data

    def update(self, instance, validated_data):
        print(instance)
        instance.set_password(validated_data['password'])
        instance.save()
        return instance

class CheckSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = []