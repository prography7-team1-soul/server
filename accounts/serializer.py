from rest_framework import serializers
from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'uuid',
            'nickname',
            'club_bookmarks',
            'chatroom_bookmarks',
            'article_bookmarks',
        ]

        read_only_fields = ['uuid', 'nickname']

    def create(self, validated_data):
        request_data = self.context.get("request")
        # uuid가 없으면 None으로 반환
        uuid = request_data.headers.get("uuid", None)
        # get으로 가져오면 오류로 다운될 수 있음
        user = User.objects.filter(uuid=uuid).first()

        if not user:
            raise serializers.ValidationError({'error_message': '이미 가입된 계쩡이 존재합니다.'})
        validated_data['uuid'] = uuid

        return super().create(validated_data)

