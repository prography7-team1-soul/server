from rest_framework import serializers

from accounts.models import User
from links.models import Link


class LinkSerializer(serializers.ModelSerializer):
    is_bookmark = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Link
        fields =[
            'title',
            'source',
            'category',
            'url',
            'is_bookmark',
        ]

        read_only_fields = ['title', 'source', 'category', 'url']

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