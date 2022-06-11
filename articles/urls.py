from django.urls import path, include
from rest_framework.routers import SimpleRouter

from articles.views import ArticleViewSet

article_router = SimpleRouter(trailing_slash=False)
article_router.register('articles', ArticleViewSet, basename='Articles')

urlpatterns = [
    path('articles', include(article_router.urls)),
]
