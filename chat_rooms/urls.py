from django.urls import path, include
from rest_framework.routers import DefaultRouter

from chat_rooms.views import ChatRoomViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'chat-rooms', ChatRoomViewSet, basename='chat-rooms')

urlpatterns = [
    path("", include(router.urls)),
]