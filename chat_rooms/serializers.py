from rest_framework import serializers

from chat_rooms.models import ChatRoom, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'name',
        )


class ChatRoomSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(read_only=True, many=True)
    class Meta:
        model = ChatRoom
        fields = (
            'id',
            'title',
            'url',
            'has_password',
            'categories',
        )