from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import User
from firebase_admin import messaging

from club.models import Club


class Notification(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    message = models.TextField()

    class PageType(models.TextChoices):
        club = 'club'
        chat_room = 'chat_room'
        article = 'article'
        profile = 'profile'

    page_type = models.CharField(
        max_length=15,
        choices=PageType.choices,
        blank=True,
        default=''
    )
    page_id = models.PositiveIntegerField(blank=True, default=True)
    is_read = models.BooleanField(default=False)


@receiver(post_save, sender=User)
def create_user_notification(sender, instance, created, **kwargs):
    if created:
        notification = Notification.objects.create(user=instance, message=f"{instance.nickname}님 가입을 축하합니다.",
                                                   page_type='profile', page_id=instance.id)
        registration_token = instance.fcm_token
        message = messaging.Message(
            notification=messaging.Notification(
                title='가입을 축하합니다.',
                body=f'{instance.nickname}',
            ),
            token=registration_token,
        )

        response = messaging.send(message)
        print('Successfully sent message:', response)


@receiver(post_save, sender=Club)
def save_club_notification(sender, instance, created, **kwargs):
    users = User.objects.all()
    for user in users:
        if instance in user.club_bookmarks.all():
            Notification.objects.create(user=user, message='club',
                                        page_type='club', page_id=instance.id)
            registration_token = user.fcm_token
            message = messaging.Message(
                notification=messaging.Notification(
                    title=f'{instance.name}동아리의 정보가 변경됐어요!',
                    body='테스트 메시지!',
                ),
                token=registration_token,
            )
            response = messaging.send(message)
            print('Successfully sent message:', response)
