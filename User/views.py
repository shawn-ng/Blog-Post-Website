from django.db import models
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated

from .serializer import UserSerializer
from .models import MyUser


class UserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer = UserSerializer
    permission_classes = [IsAuthenticated]
