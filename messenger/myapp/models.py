from django.db import models
from user.models import AuthUser
from django.utils import timezone


class Chat(models.Model):
    name_chat = models.CharField(max_length=80, default='Private')
    is_private = models.BooleanField(default=True)
    users = models.ManyToManyField(AuthUser, blank=True)

    def assign_recipient(self, user_chat):
        for u in self.users.all():
            if u != user_chat:
                self.recipient = u

class Messages(models.Model):
    chat = models.ForeignKey(
        Chat, related_name="messages", on_delete=models.CASCADE
        )
    author = models.ForeignKey(
        AuthUser, blank=True, null=True, on_delete=models.CASCADE
        )
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} {}".format(self.author, self.text)