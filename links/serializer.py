from rest_framework import serializers
from accounts.models import User
from links.models import Link, SourceField, Category


class SourceFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = SourceField
        fields = ['name', ]


class LinkDetailSerializer(serializers.ModelSerializer):
    is_bookmark = serializers.SerializerMethodField(read_only=True)
    source = SourceFieldSerializer(read_only=True, many=True)
    class Meta:
        model = Link
        fields = [
            'id',
            'title',
            'description',
            'source',
            'url',
            'is_bookmark',
        ]

        read_only_fields = ['title', 'source', 'url']

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
