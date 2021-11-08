from django.shortcuts import render
from rest_framework import viewsets

from Friend.models import Friend
from Friend.serializer import FriendSerializer
# Create your views here.


class FriendViewSet(viewsets.ModelViewSet):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer

    def create(self, request):
        print(request.data)
