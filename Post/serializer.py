from django.db import models
from rest_framework import serializers

from Post.models import Post


class PostSerializer(serializers.ModelSerializer):
    model = Post
    feild = ['post_id', 'post_id_post', 'image_url',
             'post_paragraph', 'post_description']
    depth = 2
