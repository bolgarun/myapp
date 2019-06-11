from django.db import models
from user.models import AuthUser
from datetime import datetime


class Messages(models.Model):
    sender = models.ForeignKey(AuthUser, related_name="sender", on_delete=models.CASCADE)
    receiver = models.ForeignKey(AuthUser, related_name="receiver", on_delete=models.CASCADE)
    data = models.DateTimeField(default=datetime.now)
    message = models.TextField(max_length=755)


    def __str__(self):
        return "{} {}".format(self.sender, self.receiver)



class Chat(models.Model):
    name = models.ForeignKey(Messages, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.name)
