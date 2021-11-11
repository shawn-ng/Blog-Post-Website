from django.db.models import query
from django.http.request import QueryDict
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import Serializer

from Friend.models import Friend
from Friend.serializer import FriendSerializer
# Create your views here.


class FriendViewSet(viewsets.ModelViewSet):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request):
        # creating two type of data ( two row ) this is to create a birectional graph
        friend_data_one = FriendSerializer(data=request.data)
        friend_data_two = FriendSerializer(data={
            'user_friend_id_one': request.data['user_friend_id_two'],
            'user_friend_id_two': request.data['user_friend_id_one'],
            'request_status': False
        })

        # saving the data and uploading it
        if friend_data_one.is_valid() and friend_data_two.is_valid():
            friend_data_one.save()
            friend_data_two.save()

            return Response(data=[friend_data_one.data, friend_data_two.data], status=status.HTTP_201_CREATED)

        return Response([friend_data_one.errors, friend_data_two.errors], status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        user = self.request.user.id
        data = []
        data1 = Friend.objects.filter(user_friend_id_one=user)
        data2 = Friend.objects.filter(user_friend_id_two=user)

        # storing data into the data array
        for i in data2:
            data.append(i)
        for i in data1:
            data.append(i)
        return data

    def put(self, request):
        friend = request.GET.get("id")

        friend_data = Friend.objects.get(id=friend)
        friend_data_2 = Friend.objects.get(id=float(friend) + 1)
        if float(friend) % 2 != 0:
            if request.data['request_status'] == True:
                friend_data.request_status = True
                friend_data_2.request_status = True
                friend_data.save()
                friend_data_2.save()
                return Response(data='Updated', status=status.HTTP_200_OK)

        return Response(data='Unable to update', status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        friend = request.GET.get("id")

        if float(friend) % 2 != 0:
            unfriend_data = Friend.objects.get(id=friend)
            unfriend_data_2 = Friend.objects.get(id=float(friend) + 1)

            unfriend_data.delete()
            unfriend_data_2.delete()

            return Response(data='Deleted', status=status.HTTP_200_OK)

        return Response(data='Unable to delete', status=status.HTTP_400_BAD_REQUEST)
