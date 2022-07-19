from rest_framework import serializers
from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'uuid',
            'nickname',
            'club_data',
            'chatroom_data',
            'article_data',
            'link_data',
            'education_data',
            'bookmark_count',
            'notification_count',
        ]

        read_only_fields = ['uuid', 'nickname', 'club_data', 'chatroom_data', 'article_data', 'link_data', 'education_data']

    def create(self, validated_data):
        request_data = self.context.get('request')
        # uuid가 없으면 None으로 반환
        uuid = request_data.headers.get('uuid', None)
        fcm_token = request_data.data.get('fcm_token', None)
        print(fcm_token)
        # get으로 가져오면 오류로 다운될 수 있음
        user = User.objects.filter(uuid=uuid).first()
        if user:
            if user.fcm_token == fcm_token:
                raise serializers.ValidationError({'error_message': '이미 가입된 계정이 존재합니다.'})
            else:
                user.fcm_token = fcm_token
                user.save()
                return 'save_fcm_token'
        validated_data['uuid'] = uuid
        validated_data['fcm_token'] = fcm_token
        return super().create(validated_data)
