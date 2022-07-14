from rest_framework import status, mixins
from rest_framework.decorators import api_view
from rest_framework.viewsets import GenericViewSet

from accounts.models import User
from rest_framework.response import Response

from chat_rooms.models import ChatRoom, Category
from chat_rooms.serializers import ChatRoomSerializer


@api_view(['POST'])
def is_chat_room_bookmark_view(request, pk):
    chat_room = ChatRoom.objects.get(id=pk)
    user = User.objects.filter(uuid=request.user.uuid, chatroom_bookmarks__in=[chat_room]).first()
    if user:
        user.chatroom_bookmarks.remove(chat_room)
        return Response({'message': 'delete bookmark'}, status=status.HTTP_204_NO_CONTENT)
    elif user is None:
        request.user.chatroom_bookmarks.add(chat_room)
        return Response({'message': 'add bookmark'}, status=status.HTTP_200_OK)
    return Response({'message': 'request data error'}, status=status.HTTP_400_BAD_REQUEST)


class ChatRoomListView(mixins.ListModelMixin, GenericViewSet):
    serializer_class = ChatRoomSerializer

    def get_queryset(self):
        category = self.request.query_params.get('category', None)
        if category:
            return Category.objects.filter(name=category)
        else:
            return Category.objects.all()

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response = {
            'chat_rooms_list': response.data
        }
        return Response(response, status=status.HTTP_200_OK)


