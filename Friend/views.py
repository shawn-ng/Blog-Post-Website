from re import search
from django.db.models import query
from django.http.request import QueryDict
from django.shortcuts import render
from rest_framework import request, viewsets, status, filters
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import Serializer

from Friend.models import Friend
from Friend.serializer import FriendSerializer
# Create your views here.


class FriendViewSet(viewsets.ModelViewSet):
    search_fields = ['user_friend_id_one', 'user_id_friend_two', 'id']
    filter_backends = (filters.SearchFilter,)
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user.id
        data = []
        data1 = Friend.objects.filter(user_friend_id_one=user)
        data2 = Friend.objects.filter(user_friend_id_two=user)

        data1_true = data1.filter(request_status=True)
        data2_true = data2.filter(request_status=True)
        # storing data into the data array
        for i in data2_true:
            data.append(i)
        for i in data1_true:
            data.append(i)
        return data

    def put(self, request):
        friend = request.GET.get("id")

        friend_data = Friend.objects.get(id=friend)
        friend_data_2 = Friend.objects.get(id=float(friend) - 1)
        if float(friend) % 2 == 0:
            if request.data['request_status'] == True:
                friend_data.request_status = True
                friend_data_2.request_status = True
                friend_data.save()
                friend_data_2.save()
                return Response(data='Updated', status=status.HTTP_200_OK)

        return Response(data='Unable to update', status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        friend = request.GET.get("id")

        if float(friend) % 2 == 0:
            unfriend_data = Friend.objects.get(id=friend)
            unfriend_data_2 = Friend.objects.get(id=float(friend) - 1)

            unfriend_data.delete()
            unfriend_data_2.delete()

            return Response(data='Deleted', status=status.HTTP_200_OK)

        return Response(data='Unable to delete', status=status.HTTP_400_BAD_REQUEST)
