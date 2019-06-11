from django.db import models
from django.contrib.auth.models import AbstractUser


class AuthUser(AbstractUser):    
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} {}".format(self.username, self.password)
