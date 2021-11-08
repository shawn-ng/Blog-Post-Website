from django.shortcuts import render
from rest_framework import viewsets

from Post.models import Post
from Post.serializer import PostSerializer
# Create your views here.


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
