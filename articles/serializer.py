from rest_framework import serializers

from articles.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'summary',
            'author',
            'url',
            'image',
        ]

        read_only_fields = ['summary', 'author', 'url', 'image',]
