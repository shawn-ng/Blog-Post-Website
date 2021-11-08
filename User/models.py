from django.db import models
import uuid
# Create your models here.


class User(models.Model):
    user_id = models.UUIDField(
        primary_key=True, editable=False, unique=True, default=uuid.uuid4)
    user = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
