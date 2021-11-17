from django.db.models import fields
from rest_framework import serializers
from Post.models import Post

# getting all the post


class AllUserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
