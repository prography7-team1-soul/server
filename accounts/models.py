from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(models.Model):
    uuid = models.CharField(unique=True, max_length=63)
    nickname = models.CharField(unique=True, max_length=15)
    club_bookmarks = models.ManyToManyField('club.Club')
    chatroom_bookmarks = models.ManyToManyField('chat_rooms.ChatRoom')
    article_bookmarks = models.ManyToManyField('articles.Article')
    # club_notifications = notinoti~

    @property
    def message(self):
        return "No params"

    @property
    def club_data(self):
        return self.club_bookmarks.values()

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
