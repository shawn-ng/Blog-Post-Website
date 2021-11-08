from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .serializer import UserProfileSerializers
from .models import UserProfile

# Create your views here.


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers
