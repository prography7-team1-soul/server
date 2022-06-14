from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(models.Model):
    uuid = models.CharField(unique=True, max_length=63)
    nickname = models.CharField(unique=True, max_length=15)
    club_bookmarks = models.ManyToManyField('club.Club', blank=True)
    chatroom_bookmarks = models.ManyToManyField('chat_rooms.ChatRoom', blank=True)
    article_bookmarks = models.ManyToManyField('articles.Article', blank=True)


@receiver(post_save, sender=User)
def create_user(sender, instance, created, *args, **kwargs):
    if created:
        instance.nickname = f'소울러{instance.id}'
        instance.save()
