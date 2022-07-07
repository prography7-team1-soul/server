from drf_yasg import openapi
from drf_yasg.utils import no_body, swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from articles.models import Article
from articles.serializer import ArticleSerializer


class ArticleViewSet(ReadOnlyModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    @swagger_auto_schema(operation_summary="소울 후기 리스트 API",
                         operation_description="- 응답을 위해 필요한 값이 없습니다. \n - 사용자의 인증이 필요하지 않습니다. \n - POST 요청이 불가능합니다.",
                         request_body=no_body)
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response = {
            'article_list': response.data
        }
        return Response(response)

    @swagger_auto_schema(operation_summary="소울 후기 상세보기 API",
                         operation_description="- 상세보기를 위한 데이터의 pk값이 url path에 필요합니다. \n "
                                               "- 사용자의 인증이 필요하지 않습니다. \n - POST 요청이 불가능합니다.",
                         request_body=no_body)
    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        response = {
            'article_retrieve': response.data
        }
        return Response(response)

    @swagger_auto_schema(operation_summary="소울 후기 북마크 등록 및 해제 API",
                         operation_description="- 상세보기를 위한 데이터의 pk값이 url path에 필요합니다. \n "
                                               "- 헤더에 uuid가 없을 경우 인증이 진행되지 않아 {401: 인증 실패} 에러가 발생합니다."
                                               "\n - GET 요청이 불가능합니다.",
                         manual_parameters=[
                             openapi.Parameter('uuid', openapi.IN_HEADER, description="인증을 위해 반드시 헤더에 필요합니다.",
                                               type=openapi.TYPE_STRING),
                            openapi.Parameter('bookmarks', openapi.IN_PATH, description="반드시 bookmarks가 path에 들어가야 합니다.",
                                                type=openapi.TYPE_STRING)],
                         request_body=no_body)
    @action(methods=['post'], detail=True)
    def bookmarks(self, request, *args, **kwargs):
        user = request.user
        if user.is_anonymous:
            return Response('인증되지 않은 유저입니다.', status=403)
        instance = Article.objects.get(pk=self.kwargs['pk'])
        # 유저 아티클 북마크에 해당 아티클이 있으면 북마크 취소
        if instance in user.article_bookmarks.all():
            user.article_bookmarks.remove(instance)
            user.save()
            response = {
                'message': '북마크 해제',
            }
            return Response(response, status=201)
        # 유저 아티클 북마크에 해당 아티클이 없으면 북마크 추가
        else:
            user.article_bookmarks.add(instance)
            user.save()
            response = {
                'message': '북마크 등록',
            }
            return Response(response, status=201)
