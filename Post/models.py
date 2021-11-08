from django.db import models
import uuid

from UserProfile.models import UserProfile

# Create your models here.


class Post(models.Model):
    post_id = models.UUIDField(
        primary_key=True, unique=True, editable=False, default=uuid.uuid1)
    profle_id_post = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    image_url = models.URLField(blank=True, null=True)
    post_paragraph = models.TextField(blank=True, null=True)
    post_description = models.TextField(max_length=500, blank=True, null=True)
    post_created = models.DateTimeField(auto_now_add=True)
