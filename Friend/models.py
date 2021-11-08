from django.db import models

from User.models import User
# Create your models here.


class Friend(models.Model):
    user_friend_id_one = models.ForeignKey(User, on_delete=models.CASCADE)
    user_friend_id_two = models.ForeignKey(User, on_delete=models.CASCADE)
