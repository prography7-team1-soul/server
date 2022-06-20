from rest_framework import serializers

from notifications.models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = (
            'id',
            'user',
            'message',
            'page_type',
            'page_id',
            'is_read',
        )
        read_only_fields = (
            'id',
            'user',
            'message',
            'page_type',
            'page_id',
        )


class NotificationIsReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = (
            'is_read',
        )
        read_only_fields = (
            'page_id',
        )