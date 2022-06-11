from rest_framework import serializers

from club.models import Club, RecruitmentField


class RecruitmentFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecruitmentField
        fields = (
            'name',
        )

class ClubSummarizeSerializer(serializers.ModelSerializer):
    recruitment_fields = RecruitmentFieldSerializer(many=True, read_only=True)
    class Meta:
        model = Club
        fields = (
            'id',
            'name',
            'club_description',
            'recruitment_fields',
            'image',
        )

class ClubDetailSerializer(serializers.ModelSerializer):
    recruitment_fields = RecruitmentFieldSerializer(many=True, read_only=True)
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
        )