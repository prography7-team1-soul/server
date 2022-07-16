import factory

from accounts.models import User
from articles.tests.factories import ArticleFactory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    uuid = 'test_uuid_01'
    fcm_token = 'test_token'

    @factory.post_generation
    def article_bookmarks(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for article in extracted:
                self.article_bookmarks.add(article)

    @factory.post_generation
    def club_bookmarks(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for club in extracted:
                self.article_bookmarks.add(club)

    @factory.post_generation
    def chatroom_bookmarks(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for chatroom in extracted:
                self.article_bookmarks.add(chatroom)

    @factory.post_generation
    def education_bookmarks(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for education in extracted:
                self.article_bookmarks.add(education)

    @factory.post_generation
    def link_bookmarks(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for link in extracted:
                self.article_bookmarks.add(link)

    @factory.post_generation
    def club_notifications(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for club in extracted:
                self.article_bookmarks.add(club)
