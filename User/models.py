from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
# Create your models here.


class MyUser(AbstractUser):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user_image_url = models.URLField(blank=True, null=True)
