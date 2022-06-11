from rest_framework import serializers
from articles.models import Article, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            'name',
        ]


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    tags = TagSerializer(read_only=True, many=True)

    class Meta:
        model = Article
        fields = [
            'summary',
            'author',
            'url',
            'tags',
            'image',
        ]

    def get_author(self, obj):
        return obj.author.name
