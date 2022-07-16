from rest_framework import serializers

from accounts.models import User
from club.models import Club, RecruitmentField


class RecruitmentFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecruitmentField
        fields = (
            'name',
        )


class ClubNotificationSerializer(serializers.ModelSerializer):
    recruitment_fields = RecruitmentFieldSerializer(many=True, read_only=True)
    is_bookmark = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Club
        fields = (
            'id',
            'name',
            'club_description',
            'recruitment_fields',
            'image',
            'is_bookmark',
        )

    def get_is_bookmark(self, obj):
        user = self.context.get("request").user
        if user != None:
            is_bookmark = User.objects.filter(id=user.id, club_bookmarks__in=[obj]).first()
            if is_bookmark is None:
                return False
            else:
                return True
        else:
            return False


class ClubSummarizeSerializer(serializers.ModelSerializer):
    recruitment_fields = RecruitmentFieldSerializer(many=True, read_only=True)
    is_bookmark = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Club
        fields = (
            'id',
            'name',
            'club_description',
            'recruitment_fields',
            'image',
            'is_bookmark',
            'is_recruitment',
        )

    def get_is_bookmark(self, obj):
        user = self.context.get("request").user
        print(user)
        if user != None:
            is_bookmark = User.objects.filter(id=user.id, club_bookmarks__in=[obj]).first()
            if is_bookmark is None:
                return False
            else:
                return True
        else:
            return False

class ClubDetailSerializer(serializers.ModelSerializer):
    recruitment_fields = RecruitmentFieldSerializer(many=True, read_only=True)
    is_bookmark = serializers.SerializerMethodField(read_only=True)
    is_notification = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Club
        fields = (
            'id',
            'name',
            'club_description',
            'recruitment_fields',
            'image',
            'recruitment_personnel',
            'recruitment_at',
            'activity_description',
            'activity_cost',
            'activity_area',
            'activity_period',
            'home_url',
            'sns',
            'is_recruitment',
            'is_bookmark',
            'is_notification',
        )

    def get_is_bookmark(self, obj):
        user = self.context.get("request").user
        print(user)
        if user != None:
            is_bookmark = User.objects.filter(id=user.id, club_bookmarks__in=[obj]).first()
            if is_bookmark is None:
                return False
            else:
                return True
        else:
            return False

    def get_is_notification(self, obj):
        user = self.context.get("request").user
        if user != None:
            is_bookmark = User.objects.filter(id=user.id, club_notifications__in=[obj]).first()
            if is_bookmark is None:
                return False
            else:
                return True
        else:
            return False