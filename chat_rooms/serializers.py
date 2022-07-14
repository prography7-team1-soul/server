from rest_framework import serializers

from accounts.models import User
from chat_rooms.models import ChatRoom, Category


class ChatRoomDetailSerializer(serializers.ModelSerializer):
    is_bookmark = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = ChatRoom
        fields = (
            'title',
            'url',
            'has_password',
            'is_bookmark',
        )

    def get_is_bookmark(self, obj):
        user = self.context.get("request").user
        if user != None:
            is_bookmark = User.objects.filter(id=user.id, chatroom_bookmarks__in=[obj]).first()
            if is_bookmark is None:
                return False
            else:
                return True
        else:
            return False


class ChatRoomSerializer(serializers.ModelSerializer):
    chat_rooms = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Category
        fields = (
            'category',
            'chat_rooms',
        )

    def get_chat_rooms(self, obj):
        serializer = ChatRoomDetailSerializer(obj.chatroom_set, many=True,
                                              context={'request': self.context.get('request')})
        return serializer.data
