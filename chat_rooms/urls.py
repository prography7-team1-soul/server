from django.urls import path, include
from rest_framework.routers import DefaultRouter

from chat_rooms.views import ChatRoomListView, is_chat_room_bookmark_view

urlpatterns = [
    path('chat-rooms/<int:pk>/bookmarks', is_chat_room_bookmark_view),
    path("chat-rooms", ChatRoomListView.as_view({'get': 'list'})),
]
