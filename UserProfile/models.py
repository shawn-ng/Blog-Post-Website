from django.db import models
import uuid
from User.models import User

# Create your models here.


class UserProfile(models.Model):
    profile_id = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4, unique=True)
    # on_delete models.CASCADE is when i delete this profile the reference will also be deleted
    user_id_profile = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=500, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    place_of_birth = models.CharField(max_length=50, blank=True, null=True)
    contact_number = models.IntegerField(blank=True, null=True)
