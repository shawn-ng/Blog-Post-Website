from django.db.models import fields
from rest_framework import serializers
from .models import UserProfile


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"
        depth = 2
