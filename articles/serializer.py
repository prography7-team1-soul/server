from rest_framework import serializers

from accounts.models import User
from articles.models import Article, Author, Tag


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            'author_name',
            'author_company',
            'author_part',
        )


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'name',
        )

class ArticleSerializer(serializers.ModelSerializer):
    is_bookmark = serializers.SerializerMethodField(read_only=True)
    author = AuthorSerializer(read_only=True)
    tags = TagSerializer(read_only=True, many=True)

    class Meta:
        model = Article
        fields = [
            'summary',
            'author',
            'url',
            'image',
            'is_bookmark',
            'tags',
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
