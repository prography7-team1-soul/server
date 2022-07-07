from rest_framework import serializers

from links.models import Link


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields =[
            'title',
            'source',
            'category',
            'url',
        ]

        read_only_fields = ['title', 'source', 'category', 'url']
