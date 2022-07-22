from rest_framework import serializers

from accounts.models import User
from educations.models import Education, RecruitmentField, SNS


class SnsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SNS
        fields = (
            'id',
            'image',
            'link',
        )


class RecruitmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecruitmentField
        fields = (
            'name',
        )


class EducationSummarizeSerializer(serializers.ModelSerializer):
    recruitment_fields = RecruitmentSerializer(many=True, read_only=True)
    is_bookmark = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Education
        fields = (
            'id',
            'name',
            'education_description',
            'recruitment_fields',
            'image',
            'is_bookmark',
            'is_recruitment',
        )

    def get_is_bookmark(self, obj):
        user = self.context.get("request").user
        print(user)
        if user != None:
            is_bookmark = User.objects.filter(id=user.id, education_bookmarks__in=[obj]).first()
            if is_bookmark is None:
                return False
            else:
                return True
        else:
            return False


class EducationNotificationSerializer(serializers.ModelSerializer):
    recruitment_fields = RecruitmentSerializer(many=True, read_only=True)
    is_bookmark = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Education
        fields = (
            'id',
            'name',
            'education_description',
            'recruitment_fields',
            'is_bookmark',
        )

    def get_is_bookmark(self, obj):
        user = self.context.get("request").user
        if user != None:
            is_bookmark = User.objects.filter(id=user.id, education_bookmarks__in=[obj]).first()
            if is_bookmark is None:
                return False
            else:
                return True
        else:
            return False


class EducationDetailSerializer(serializers.ModelSerializer):
    recruitment_fields = RecruitmentSerializer(many=True, read_only=True)
    is_bookmark = serializers.SerializerMethodField(read_only=True)
    is_notification = serializers.SerializerMethodField(read_only=True)
    sns = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Education
        fields = (
            'id',
            'name',
            'description',
            'recruitment_fields',
            'image',
            'recruitment_personnel',
            'recruitment_at',
            'education_description',
            'education_cost',
            'education_area',
            'education_period',
            'home_url',
            'sns',
            'is_bookmark',
            'is_recruitment',
            'is_notification',
            'detail_image',
        )

    def get_is_bookmark(self, obj):
        user = self.context.get("request").user
        if user != None:
            is_bookmark = User.objects.filter(id=user.id, education_bookmarks__in=[obj]).first()
            if is_bookmark is None:
                return False
            else:
                return True
        else:
            return False

    def get_is_notification(self, obj):
        user = self.context.get("request").user
        if user != None:
            is_bookmark = User.objects.filter(id=user.id, education_notifications__in=[obj]).first()
            if is_bookmark is None:
                return False
            else:
                return True
        else:
            return False

    def get_sns(self, obj):
        sns = obj.sns_set
        serializer = SnsSerializer(sns, many=True)
        return serializer.data