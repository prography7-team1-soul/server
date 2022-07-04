from rest_framework import serializers


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        fields =[
            'title',
            'source',
            'category',
            'url',
        ]

        read_only_fields = ['title', 'source', 'category', 'url']
