from django.shortcuts import render
from rest_framework import viewsets, filters
from django.contrib.auth import get_user_model

from .serializer import SearchUserSerializer
# Create your views here.


class SearchUserView(viewsets.ModelViewSet):
    search_fields = ['username', 'first_name', 'last_name', 'id']
    filter_backends = (filters.SearchFilter,)
    queryset = get_user_model().objects.all()
    serializer_class = SearchUserSerializer
