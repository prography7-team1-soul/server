from rest_framework import serializers

from club.models import Club, RecruitmentField


class ClubRecruitmentFields(serializers.ModelSerializer):
    class Meta:
        model = RecruitmentField
        fields = (
            'name',
        )


class ClubBookmarkSerializer(serializers.ModelSerializer):
    recruitment_fields = ClubRecruitmentFields(read_only=True, many=True)
    class Meta:
        model = Club
        fields = (
            'id',
            'name',
            'image',
            'recruitment_fields',

        )
