from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializer import UserProfileSerializers
from .models import UserProfile

# Create your views here.


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers
    permission_classes = [IsAuthenticated]

    # this is to only get the login user profile
    def get_queryset(self):
        user = self.request.user
        data = UserProfile.objects.filter(user_id_profile=user)
        return data
