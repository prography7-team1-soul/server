from rest_framework import serializers

from accounts.models import User
from educations.models import Education, RecruitmentField


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


class EducationDetailSerializer(serializers.ModelSerializer):
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
            'recruitment_personnel',
            'recruitment_at',
            'education_description',
            'education_cost',
            'education_area',
            'education_period',
            'home_url',
            'sns',
            'is_bookmark',
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