from rest_framework import serializers

from server.chat_rooms.models import ChatRoom, Category


class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = (
            'id',
            'title',
            'url',
            'has_password',
            'category_list',
        )