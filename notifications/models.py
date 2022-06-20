from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import User
from firebase_admin import messaging

from club.models import Club


class Notification(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    message = models.TextField()


@receiver(post_save, sender=User)
def create_user_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(user=instance, message=f"{instance.nickname}님 가입을 축하합니다.")
        registration_token = instance.fcm_token
        message = messaging.Message(
            notification=messaging.Notification(
                title='안녕하세요 테스트 메시지 입니다.',
                body='테스트 메시지!',
            ),
            token=registration_token,
        )

        response = messaging.send(message)
        print('Successfully sent message:', response)


@receiver(post_save, sender=Club)
def save_club_notification(sender, instance, created, **kwargs):
    users = User.objects.all()
    for user in users:
        if instance in user.club_bookmarks:
            Notification.objects.create(user=user, message='club')
            registration_token = user.fcm_token
            message = messaging.Message(
                notification=messaging.Notification(
                    title='클럽 테스트 메시지입니다.',
                    body='테스트 메시지!',
                ),
                token=registration_token,
            )
        response = messaging.send(message)
        print('Successfully sent message:', response)
