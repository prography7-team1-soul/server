from rest_framework.viewsets import ReadOnlyModelViewSet
from articles.models import Article
from articles.serializer import ArticleSerializer


class ArticleViewSet(ReadOnlyModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

