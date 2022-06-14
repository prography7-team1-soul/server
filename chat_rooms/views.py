from rest_framework import viewsets, status
from rest_framework.decorators import action
from accounts.models import User
from rest_framework.response import Response

from chat_rooms.models import ChatRoom
from chat_rooms.serializers import ChatRoomSerializer


class ChatRoomViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer

    @action(methods=['post'], detail=True)
    def bookmark(self, request, pk):
        chat_room = self.get_object()
        user = User.objects.filter(uuid=request.user.uuid, chatroom_bookmarks__in=[chat_room]).first()
        if user:
            user.chatroom_bookmarks.remove(chat_room)
            return Response({'message': 'delete bookmark'}, status=status.HTTP_204_NO_CONTENT)
        elif user is None:
            request.user.chatroom_bookmarks.add(chat_room)
            return Response({'message': 'add bookmark'}, status=status.HTTP_200_OK)
        return Response({'message': 'request data error'}, status=status.HTTP_400_BAD_REQUEST)
