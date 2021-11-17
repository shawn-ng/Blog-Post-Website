from rest_framework import serializers
from django.contrib.auth import get_user_model


class SearchUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'password',
                  'first_name', 'last_name', 'email')
