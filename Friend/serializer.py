from rest_framework import serializers

from Friend.models import Friend


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = "__all__"
        depth = 2
