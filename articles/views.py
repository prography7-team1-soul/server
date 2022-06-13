from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from articles.models import Article
from articles.serializer import ArticleSerializer


class ArticleViewSet(ReadOnlyModelViewSet):
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


class ArticleBookmarkViewSet(ModelViewSet):
    serializer_class = ArticleSerializer

    @action(methods=['post'], detail=False)
    def bookmark(self, request, *args, **kwargs):
        user = request.user
        instance = Article.objects.get(pk=self.kwargs['article_pk'])
        # 유저 아티클 북마크에 해당 아티클이 있으면 북마크 취소
        if instance in user.article_bookmarks.all():
            user.article_bookmarks.remove(instance)
        # 유저 아티클 북마크에 해당 아티클이 없으면 북마크 추가
        else:
            user.article_bookmarks.add(instance)
        user.save()
        return Response("북마크 작동 성공~", status=201)

