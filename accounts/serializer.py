from rest_framework import serializers
from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'uuid',
            'nickname',
        ]

        read_only_fields = ['uuid', 'nickname']

    def create(self, validated_data):
        request_data = self.context.get('request')
        # uuid가 없으면 None으로 반환
        uuid = request_data.headers.get('uuid', None)
        # get으로 가져오면 오류로 다운될 수 있음
        user = User.objects.filter(uuid=uuid).first()
        if user:
            raise serializers.ValidationError({'error_message': '이미 가입된 계정이 존재합니다.'})
        validated_data['uuid'] = uuid
        return super().create(validated_data)


class UserBookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'club_bookmarks',
            'chatroom_bookmarks',
            'article_bookmarks',
        ]

        read_only_fields = ['club_bookmarks', 'chatroom_bookmarks', 'article_bookmarks']


class UserClubBookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'club_bookmarks',
        ]


class UserChatroomBookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'chatroom_bookmarks',
        ]


class UserArticleBookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'article_bookmarks',
        ]
