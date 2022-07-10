from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView
from articles.models import Article
from articles.serializer import ArticleSerializer
from chat_rooms.models import ChatRoom
from chat_rooms.serializers import ChatRoomSerializer
from club.models import Club
from club.serializers import ClubSummarizeSerializer
from educations.models import Education
from educations.serializers import EducationDetailSerializer
from links.models import Link
from links.serializer import LinkSerializer


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

    def get_link_objects(self, search_param):
        objects = Link.objects.filter(
            Q(title__icontains=search_param) |
            Q(source__name__icontains=search_param) |
            Q(category__name__icontains=search_param)
        ).distinct()

        serializer = LinkSerializer(objects, many=True)
        return serializer.data

    def get_education_objects(self, search_param):
        objects = Education.objects.filter(
            Q(name__icontains=search_param) |
            Q(description__icontains=search_param) |
            Q(recruitment_fields__name__icontains=search_param)
        ).distinct()

        serializer = EducationDetailSerializer(objects, many=True)
        return serializer.data

    def get(self, request):
        search_param = request.query_params.get('search_param', None)
        app = request.query_params.get('app', None)
        if not search_param:
            return Response('검색어가 없습니다.', status=400)
        if app:
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
            elif app == 'link':
                response = {
                    'link_search_list': self.get_link_objects(search_param),
                }
            elif app == 'education':
                response = {
                    'education_search_list': self.get_education_objects(search_param),
                }
            else:
                return Response('app 이름을 다시 한번 확인해주세요.', status=400)
        else:
            response = {
                    'club_search_list': self.get_club_objects(search_param),
                    'article_search_list': self.get_article_objects(search_param),
                    'chatroom_search_list': self.get_chatroom_objects(search_param),
                    'link_search_list': self.get_link_objects(search_param),
                    'education_search_list': self.get_education_objects(search_param),
            }
        return Response(response, status=200)
