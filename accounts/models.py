from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(models.Model):
    uuid = models.CharField(unique=True, max_length=63)
    nickname = models.CharField(unique=True, max_length=15)
    club_bookmarks = models.ManyToManyField('club.Club', blank=True)
    chatroom_bookmarks = models.ManyToManyField('chat_rooms.ChatRoom', blank=True)
    article_bookmarks = models.ManyToManyField('articles.Article', blank=True)
    fcm_token = models.TextField(blank=True, default='', null=True)

    @property
    def club_data(self):
        return self.club_bookmarks.values() # 필드 추가될 수 있음

    @property
    def chatroom_data(self):
        return self.chatroom_bookmarks.values()

    @property
    def article_data(self):
        return self.article_bookmarks.values()


@receiver(post_save, sender=User)
def create_user(sender, instance, created, *args, **kwargs):
    if created:
        instance.nickname = f'소울러{instance.id}'
        instance.save()
