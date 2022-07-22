from rest_framework import serializers

from articles.models import Article, Author
from chat_rooms.models import ChatRoom
from club.models import Club, RecruitmentField
from educations.models import Education, RecruitmentField as E
from links.models import Link, Tag, Source


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


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            'author_name',
            'author_company',
            'author_part',
        )


class ArticleBookmarkSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Article
        fields = (
            'id',
            'summary',
            'url',
            'image',
            'author',
        )


class LinkTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'name',
        )


class LinkBookmarkSerializer(serializers.ModelSerializer):
    tags = LinkTagSerializer(read_only=True, many=True)
    class Meta:
        model = Link
        fields = (
            'id',
            'title',
            'url',
            'source_name',
            'tags',
            'category_id',
        )


class EducationRecruitmentFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = E
        fields = (
            'name',
        )


class EducationBookmarkSerializer(serializers.ModelSerializer):
    recruitment_fields = EducationRecruitmentFieldSerializer(read_only=True, many=True)

    class Meta:
        model = Education
        fields = (
            'id',
            'name',
            'image',
            'description',
            'recruitment_personnel',
            'recruitment_at',
            'education_description',
            'education_cost',
            'education_area',
            'education_period',
            'home_url',
            'detail_image',
            'recruitment_fields',
        )
