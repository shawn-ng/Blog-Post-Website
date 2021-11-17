from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import json

from Post.models import Post
from .serializer import AllUserPostSerializer
from Post.serializer import PostSerializer
# Create your views here.


class AllUserPostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, pk):
        post_data = Post.objects.filter(profile_id=pk)

        serialize_data = AllUserPostSerializer(post_data, many=True)

        return Response(serialize_data.data, status.HTTP_200_OK)
