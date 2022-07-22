from rest_framework import serializers

from articles.models import Article
from chat_rooms.models import ChatRoom
from club.models import Club, RecruitmentField
from educations.models import Education
from links.models import Link


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


class ChatRoomBookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = (
            'id',
            'title',
            'url',
            'has_password',
            'image',
            'category_id',
        )


class ArticleBookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            'id',
            'summary',
            'url',
            'image',
        )


class LinkBookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = (
            'id',
            'title',
            'url',
        )


class EducationBookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = (
            'id',
            'name',
            'image',
        )