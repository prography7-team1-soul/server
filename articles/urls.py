from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter

from articles.views import ArticleViewSet, ArticleBookmarkViewSet

article_router = SimpleRouter(trailing_slash=False)
article_router.register('articles', ArticleViewSet, basename='Articles')

article_bookmark_router = SimpleRouter(trailing_slash=False)
article_bookmark_router.register('', ArticleBookmarkViewSet, basename='Article-Bookmark')

urlpatterns = [
    path('', include(article_router.urls)),
    path('article/<int:article_pk>/', include(article_bookmark_router.urls)),
]
