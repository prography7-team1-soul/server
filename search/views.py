from django.db.models import Q
from rest_framework.mixins import ListModelMixin
from django.shortcuts import render

# Create your views here
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from articles.models import Article
from articles.serializer import ArticleSerializer
from chat_rooms.models import ChatRoom
from chat_rooms.serializers import ChatRoomSerializer
from club.models import Club
from club.serializers import ClubSummarizeSerializer


class ArticleSearchViewSet(ListModelMixin, GenericViewSet):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        search_param = self.request.query_params['search_param']
        article = Article.objects.filter(
            Q(summary__icontains=search_param) |
            Q(tags__name__icontains=search_param) |
            Q(author__company__name__icontains=search_param) |
            Q(author__part__name__icontains=search_param))

        return article

    def list(self, request, *args, **kwargs):
        response = super().list(self, request, *args, **kwargs)
        response = {
            'article_search_list': response.data,
        }
        return Response(response)


class ClubSearchViewSet(ListModelMixin, GenericViewSet):
    serializer_class = ClubSummarizeSerializer

    def get_queryset(self):
        search_param = self.request.query_params['search_param']
        club = Club.objects.filter(
            Q(name__icontains=search_param) |
            Q(recruitment_fields__name__icontains=search_param) |
            Q(club_description__icontains=search_param)
        )
        return club

    def list(self, request, *args, **kwargs):
        response = super().list(self, request, *args, **kwargs)
        response = {
            'club_search_list': response.data,
        }
        return Response(response)


class ChatRoomSearchViewSet(ListModelMixin, GenericViewSet):
    serializer_class = ChatRoomSerializer

    def get_queryset(self):
        search_param = self.request.query_params['search_param']
        chat_rooms = ChatRoom.objects.filter(
            Q(title__icontains=search_param) |
            Q(categories__name__icontains=search_param)
        )
        return chat_rooms

    def list(self, request, *args, **kwargs):
        response = super().list(self, request, *args, **kwargs)
        response = {
            'chatroom_search_list': response.data,
        }
        return Response(response)
