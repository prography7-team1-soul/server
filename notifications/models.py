from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import User


class Notification(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    message = models.TextField()


@receiver(post_save, sender=User)
def create_user_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(user=instance, message=f"{instance.nickname}님 가입을 축하합니다.")
