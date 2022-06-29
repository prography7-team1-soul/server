from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import User
from firebase_admin import messaging

from club.models import Club


class Notification(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    message = models.TextField()



