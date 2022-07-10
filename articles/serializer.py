from rest_framework import serializers

from accounts.models import User
from articles.models import Article, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            'name',
            'company',
            'part',
        )


class ArticleSerializer(serializers.ModelSerializer):
    is_bookmark = serializers.SerializerMethodField(read_only=True)
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Article
        fields = [
            'summary',
            'author',
            'url',
            'image',
            'is_bookmark',
        ]

        read_only_fields = ['summary', 'author', 'url', 'image',]

    def get_is_bookmark(self, obj):
        user = self.context.get("request").user
        print(user)
        if user != None:
            is_bookmark = User.objects.filter(id=user.id, article_bookmarks__in=[obj]).first()
            if is_bookmark is None:
                return False
            else:
                return True
        else:
            return False
