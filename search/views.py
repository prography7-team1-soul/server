from django.db.models import Q
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from articles.models import Article
from articles.serializer import ArticleSerializer
from chat_rooms.models import ChatRoom
from chat_rooms.serializers import ChatRoomSerializer
from club.models import Club
from club.serializers import ClubSummarizeSerializer


"""class ArticleSearchViewSet(ListModelMixin, GenericViewSet):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        search_param = self.request.query_params['search_param']
        article = Article.objects.filter(
            Q(summary__icontains=search_param) |
            Q(tags__name__icontains=search_param) |
            Q(author__company__name__icontains=search_param) |
            Q(author__part__name__icontains=search_param)
        ).distinct()
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
            Q(club_description__icontains=search_param) |
            Q(recruitment_fields__name__icontains=search_param)
        ).distinct()

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
        ).distinct()
        return chat_rooms

    def list(self, request, *args, **kwargs):
        response = super().list(self, request, *args, **kwargs)
        response = {
            'chatroom_search_list': response.data,
        }
        return Response(response)"""


class SearchView(APIView):
    def get_club_objects(self, search_param):
        objects = Club.objects.filter(
                Q(name__contains=search_param) |
                Q(club_description__contains=search_param) |
                Q(recruitment_fields__name__contains=search_param)
            ).distinct()
        serializer = ClubSummarizeSerializer(objects, many=True)
        return serializer.data

    def get_chatroom_objects(self, search_param):
        objects = ChatRoom.objects.filter(
                Q(title__icontains=search_param) |
                Q(categories__name__icontains=search_param)
            ).distinct()
        serializer = ChatRoomSerializer(objects, many=True)
        return serializer.data

    def get_article_objects(self, search_param):
        objects = Article.objects.filter(
                Q(summary__icontains=search_param) |
                Q(tags__name__icontains=search_param) |
                Q(author__company__name__icontains=search_param) |
                Q(author__part__name__icontains=search_param)
            ).distinct()
        serializer = ArticleSerializer(objects, many=True)
        return serializer.data

    def get(self, request):
        response = {}
        search_param = request.query_params['search_param']
        if not search_param:
            return Response('검색어가 없습니다.')
        if request.query_params['app']:
            app = request.query_params['app']
            if app == 'club':
                response = {
                    'club_search_list': self.get_club_objects(search_param),
                }
            elif app == 'chatroom':
                response = {
                    'chatroom_search_list': self.get_chatroom_objects(search_param),
                }
            elif app == 'article':
                response = {
                    'article_search_list': self.get_article_objects(search_param),
                }
            elif app == 'all':
                response = {
                    'club_search_list': self.get_club_objects(search_param),
                    'articles_search_list': self.get_article_objects(search_param),
                    'chatrooms_search_list': self.get_chatroom_objects(search_param),
                }
            return Response(response)
