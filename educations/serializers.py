from rest_framework import serializers

from educations.models import Education, RecruitmentField


class RecruitmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecruitmentField
        fields = (
            'name',
        )


class EducationSummarizeSerializer(serializers.ModelSerializer):
    recruitment_fields = RecruitmentSerializer(many=True, read_only=True)

    class Meta:
        model = Education
        fields = (
            'id',
            'name',
            'education_description',
            'recruitment_fields',
            'image',
        )


class EducationDetailSerializer(serializers.ModelSerializer):
    recruitment_fields = RecruitmentSerializer(many=True, read_only=True)

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
        )