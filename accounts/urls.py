from django.urls import path, include
from rest_framework.routers import SimpleRouter
from accounts.views import UserDetailViewSet, UserBookmarkViewSet

user_router = SimpleRouter(trailing_slash=False)
user_router.register('users', UserDetailViewSet, basename='User')

user_bookmarks_router = SimpleRouter(trailing_slash=False)
user_bookmarks_router.register('bookmarks', UserBookmarkViewSet, basename='user-bookmarks')

urlpatterns = [
    path('', include(user_router.urls)),
    path('users/<int:user_pk>/', include(user_bookmarks_router.urls)),
]
