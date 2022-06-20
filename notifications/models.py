from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import User
from firebase_admin import messaging


class Notification(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    message = models.TextField()


@receiver(post_save, sender=User)
def create_user_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(user=instance, message=f"{instance.nickname}님 가입을 축하합니다.")
        registration_token = 'cM9Uwmb3JU_DkeIewiua0C:APA91bHx7_JoHBKp4oY3I2CcSVgc9wyhfkx9w22c6ZaA17wWg0514MCnyDvq0pqL3VoPriD9U6XFYRKA-31Cn_BdwsyuE4pqyvbxSykSJFVmU9OWMluluMwIvVjb-G81UJTPCn5yVpPM'
        message = messaging.Message(
            notification=messaging.Notification(
                title='안녕하세요 테스트 메시지 입니다.',
                body='테스트 메시지!',
            ),
            token=registration_token,
        )

        response = messaging.send(message)
        print('Successfully sent message:', response)
