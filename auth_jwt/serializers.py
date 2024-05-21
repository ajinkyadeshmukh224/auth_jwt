from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser


class CustomTokenObtainSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    application = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        application = attrs.get('application')

        user = authenticate(username=username, password=password)

        # if user is not None and user.application == application:
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return {
                'refresh_token': str(refresh),
                'access_token': str(refresh.access_token),
            }
        else:
            raise serializers.ValidationError('Invalid credentials or application')
