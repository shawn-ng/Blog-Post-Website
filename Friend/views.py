from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from Friend.models import Friend
from Friend.serializer import FriendSerializer
# Create your views here.


class FriendViewSet(viewsets.ModelViewSet):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer

    def create(self, request):
        # {'user_friend_id_one': 'cf48c865-2db7-4be4-9006-d5595fca829d', 'user_friend_id_two': '35367163-c482-401d-b621-4c90f62594f6'}
        friend_data_one = FriendSerializer(data=request.data)
        friend_data_two = FriendSerializer(data={
            'user_friend_id_one': request.data['user_friend_id_two'],
            'user_friend_id_two': request.data['user_friend_id_one']
        })

        if friend_data_one.is_valid() and friend_data_two.is_valid():
            friend_data_one.save()
            friend_data_two.save()

            return Response(data=[friend_data_one.data, friend_data_two.data], status=status.HTTP_201_CREATED)

        return Response([friend_data_one.errors, friend_data_two.errors], status=status.HTTP_400_BAD_REQUEST)
