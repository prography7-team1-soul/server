from django.urls import path, include
from rest_framework.routers import SimpleRouter

from search.views import ArticleSearchViewSet, ClubSearchViewSet, ChatRoomSearchViewSet

article_search_router = SimpleRouter(trailing_slash=False)
article_search_router.register('articles', ArticleSearchViewSet, basename='Article-Search')

club_search_router = SimpleRouter(trailing_slash=False)
club_search_router.register('club', ClubSearchViewSet, basename='Club-Search')

chatroom_search_router = SimpleRouter(trailing_slash=False)
chatroom_search_router.register('chatrooms', ChatRoomSearchViewSet, basename='ChatRoom-Search')

urlpatterns=[
    path('search/', include(article_search_router.urls)),
    path('search/', include(club_search_router.urls)),
    path('search/', include(chatroom_search_router.urls)),
]
