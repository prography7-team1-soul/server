from rest_framework import serializers
from accounts.models import User
from links.models import Link, Source, Category, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = [
            'id',
            'name',
        ]


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = [
            'id',
            'name',
        ]


class LinkDetailSerializer(serializers.ModelSerializer):
    is_bookmark = serializers.SerializerMethodField(read_only=True)
    tags = TagSerializer(read_only=True, many=True)
    source = SourceSerializer(read_only=True)

    class Meta:
        model = Link
        fields = [
            'id',
            'title',
            'source',
            'tags',
            'url',
            'is_bookmark',
        ]

        read_only_fields = ['title', 'source', 'url', 'tags', 'id']

    def get_is_bookmark(self, obj):
        user = self.context.get("request").user
        print(user)
        if user != None:
            is_bookmark = User.objects.filter(id=user.id, link_bookmarks__in=[obj]).first()
            if is_bookmark is None:
                return False
            else:
                return True
        else:
            return False


class LinkSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Category
        fields = [
            'id',
            'category',
            'description',
            'links',
        ]

    def get_links(self, obj):
        serializer = LinkDetailSerializer(obj.link_set, many=True, context={'request':self.context.get('request')})
        return serializer.data
