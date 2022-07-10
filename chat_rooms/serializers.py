from rest_framework import serializers

from accounts.models import User
from chat_rooms.models import ChatRoom, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'name',
        )


class ChatRoomSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(read_only=True, many=True)
    is_bookmark = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = ChatRoom
        fields = (
            'id',
            'title',
            'url',
            'has_password',
            'categories',
            'is_bookmark',
        )

    def get_is_bookmark(self, obj):
        user = self.context.get("request").user
        print(user)
        if user != None:
            is_bookmark = User.objects.filter(id=user.id, chatroom_bookmarks__in=[obj]).first()
            if is_bookmark is None:
                return False
            else:
                return True
        else:
            return False