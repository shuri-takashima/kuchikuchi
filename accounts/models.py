from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    username = models.CharField(unique=True, max_length =25)
    email = models.EmailField(unique=True)
    avatar = models.ImageField(
        upload_to='avatar/',
    )

    USERNAME_FIELD ='email'
    REQUIRED_FIELDS = ['username']


class Connection(models.Model):
    following=models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='connection_following')
    follower = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='connection_follower')

    def __str__(self):
        return self.following.username + 'follow' +self.follower.username
