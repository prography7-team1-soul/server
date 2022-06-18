from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from articles.models import Article
from articles.serializer import ArticleSerializer


class ArticleViewSet(ReadOnlyModelViewSet):
    """
    소울 후기 리스트 및 1개 조회 API

    ---
    ## `/api/articles/<pk>/bookmark`
        - /api/articles
        - /api/articles/<pk>
        - bookmark가 들어가면 북마크 기능 작동
    ## 요청 메소드
        - 리스트 및 1개 조회는 GET만 가능합니다.
        - Bookmark 등록 또는 해제에 한해 POST 메소드 가능합니다.
    ## 에러 메시지
        - 인증되지 않은 유저의 경우 북마크 이용 시 401 UnAuthorized 에러가 발생합니다.
        - 조회는 인증 없이 모든 유저가 사용 가능합니다.
    ## 내용
        - summary: 소울 후기 내용 요약
        - author: 후기 작성자(현직자)
        - url: notion 링크
        - image: 소울 후기 이미지
    """
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response = {
            'article_list': response.data
        }
        return Response(response)

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        response = {
            'article_data': response.data
        }
        return Response(response)

    @action(methods=['post'], detail=True)
    def bookmark(self, request, *args, **kwargs):
        user = request.user
        if user is None:
            return Response('인증되지 않은 유저입니다.', status=401)
        instance = Article.objects.get(pk=self.kwargs['pk'])
        # 유저 아티클 북마크에 해당 아티클이 있으면 북마크 취소
        if instance in user.article_bookmarks.all():
            user.article_bookmarks.remove(instance)
            user.save()
            return Response('북마크 해제', status=201)
        # 유저 아티클 북마크에 해당 아티클이 없으면 북마크 추가
        else:
            user.article_bookmarks.add(instance)
            user.save()
            return Response('북마크 등록', status=201)
