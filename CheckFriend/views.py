from django.shortcuts import render
from django.views.generic.base import View
from rest_framework import request, viewsets, filters, status
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from Friend.models import Friend
from .searializer import CheckFriendSerializer, PeddingFriendSerializer
# Create your views here.


class CheckFriendViewSet (viewsets.ModelViewSet):
    search_fields = ['user_friend_id_one__id', 'user_friend_id_two__id']
    filter_backends = (filters.SearchFilter,)
    queryset = Friend.objects.all()
    serializer_class = CheckFriendSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user.id

        data = Friend.objects.filter(user_friend_id_one=user)

        return data.filter(request_status=True)

    def create(self, request):
        friend_data_one = CheckFriendSerializer(data={
            'user_friend_id_one': self.request.user.id,
            'user_friend_id_two': request.data['user_friend_id_two'],
            'request_status': False,
            'who_send': self.request.user.id
        })

        friend_data_two = CheckFriendSerializer(data={
            'user_friend_id_one': request.data['user_friend_id_two'],
            'user_friend_id_two': self.request.user.id,
            'request_status': False,
            'who_send': self.request.user.id
        })

        if friend_data_one.is_valid() and friend_data_two.is_valid():
            friend_data_one.save()
            friend_data_two.save()

            return Response(data=[friend_data_one.data, friend_data_two.data], status=status.HTTP_201_CREATED)

        return Response([friend_data_one.errors, friend_data_two.errors], status=status.HTTP_400_BAD_REQUEST)


class CheckPendingFriendViewSet(viewsets.ModelViewSet):
    queryset = Friend.objects.all()
    serializer_class = CheckFriendSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user.id

        data = Friend.objects.filter(user_friend_id_one=user)

        return data.filter(request_status=False)


class CheckFriendStatusViewSet (viewsets.ModelViewSet):
    queryset = Friend.objects.all()
    serializer_class = PeddingFriendSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user.id

        data = Friend.objects.filter(user_friend_id_one=user)

        return data.filter(request_status=False)
