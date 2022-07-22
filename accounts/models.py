from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.serializers_util import ClubBookmarkSerializer, ChatRoomBookmarkSerializer, ArticleBookmarkSerializer, \
    LinkBookmarkSerializer, EducationBookmarkSerializer


class User(models.Model):
    uuid = models.CharField(unique=True, max_length=63)
    nickname = models.CharField(unique=True, max_length=15)
    club_bookmarks = models.ManyToManyField('club.Club', blank=True)
    chatroom_bookmarks = models.ManyToManyField('chat_rooms.ChatRoom', blank=True)
    article_bookmarks = models.ManyToManyField('articles.Article', blank=True)
    education_bookmarks = models.ManyToManyField('educations.Education', blank=True)
    link_bookmarks = models.ManyToManyField('links.Link', blank=True)
    fcm_token = models.TextField(blank=True, default='', null=True)
    club_notifications = models.ManyToManyField('club.Club', blank=True, related_name='user_club_notifications')
    education_notifications = models.ManyToManyField('educations.Education', blank=True,
                                                     related_name='user_education_notifications')

    @property
    def club_data(self):
        queryset = self.club_bookmarks.all()
        serializer = ClubBookmarkSerializer(queryset, many=True)
        return serializer.data

    @property
    def chatroom_data(self):
        queryset = self.chatroom_bookmarks.all()
        serializer = ChatRoomBookmarkSerializer(queryset, many=True)
        return serializer.data

    @property
    def article_data(self):
        queryset = self.article_bookmarks.all()
        serializer = ArticleBookmarkSerializer(queryset, many=True)
        return serializer.data

    @property
    def link_data(self):
        queryset = self.link_bookmarks.all()
        serializer = LinkBookmarkSerializer(queryset, many=True)
        return serializer.data

    @property
    def education_data(self):
        queryset = self.education_bookmarks.all()
        serializer = EducationBookmarkSerializer(queryset, many=True)
        return serializer.data

    @property
    def is_anonymous(self):
        return False

    @property
    def bookmark_count(self):
        return self.club_bookmarks.count() + self.article_bookmarks.count() + self.chatroom_bookmarks.count() \
               + self.education_bookmarks.count() + self.link_bookmarks.count()

    @property
    def notification_count(self):
        return self.education_notifications.count() + self.club_notifications.count()


@receiver(post_save, sender=User)
def create_user(sender, instance, created, *args, **kwargs):
    if created:
        instance.nickname = f'소울러{instance.id}'
        instance.save()
