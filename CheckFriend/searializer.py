from django.db.models import fields
from rest_framework import serializers

from Friend.models import Friend


class CheckFriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = "__all__"


class PeddingFriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = ["user_friend_id_two", "id", "who_send"]
        depth = 1
