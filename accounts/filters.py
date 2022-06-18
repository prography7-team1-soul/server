from rest_framework.filters import BaseFilterBackend


class BookmarkFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        if request.query_params.get('app') == 'club':
            return queryset.only('club_bookmarks')
        elif request.query_params.get('app') == 'article':
            return queryset.only('article_bookmarks')
        elif request.query_params.get('app') == 'chatroom':
            return queryset.only('chatroom_bookmarks')
