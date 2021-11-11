from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from .serializer import RegisterSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model

# Register API


class RegisterApi(CreateAPIView):

    model = get_user_model()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = RegisterSerializer
