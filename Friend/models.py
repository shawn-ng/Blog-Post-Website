from django.db import models
from django.conf import settings

# Create your models here.


class Friend(models.Model):
    user_friend_id_one = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_friend_id_one')
    user_friend_id_two = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_friend_id_two')
