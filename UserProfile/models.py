from django.db import models
import uuid
from django.conf import settings

# Create your models here.


class UserProfile(models.Model):
    profile_id = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4, unique=True)
    # on_delete models.CASCADE is when i delete the user the reference/ user profile will also be deleted
    user_id_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_name = models.CharField(max_length=50, blank=True, null=True)
    profile_image_url = models.URLField(blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    place_of_birth = models.CharField(max_length=50, blank=True, null=True)
    contact_number = models.IntegerField(blank=True, null=True)
    private = models.BooleanField(default=False)
