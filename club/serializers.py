from rest_framework import serializers

from server.club.models import Club


class ClubSummarizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = (
            'id',
            'name',
            'club_description',
            'recruitment_fields',
        )