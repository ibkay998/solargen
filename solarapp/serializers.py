from rest_framework import serializers
from .models import Installer,UserProfile
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model
from .models import Installer, UserProfile

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token

class InstallerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Installer
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'users']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'installer']

class SignInSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            # Retrieve the user object using the provided username
            
            try:
                user = Installer.objects.get(username=username)
            except Installer.DoesNotExist:
                raise serializers.ValidationError('Invalid credentials1')

            # Check if the provided password matches the user's password
            print(password,user.password,"password")
            if not check_password(password, user.password):

                raise serializers.ValidationError('Invalid credentials2')
            
            # If authentication successful, return the user
            data['user'] = user
            return data
        else:
            raise serializers.ValidationError('Username and password are required')

class UserProfileSignInSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)