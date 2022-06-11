from django.db import models


class ChatRoom(models.Model):
    title = models.CharField(max_length=31)
    url = models.URLField()
    has_password = models.BooleanField(default=False)
    # field

