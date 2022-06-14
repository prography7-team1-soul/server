from rest_framework import viewsets, status
from club.models import Club
from club.serializers import ClubSummarizeSerializer
from rest_framework.decorators import action
from club.serializers import ClubDetailSerializer
from accounts.models import User
from rest_framework.response import Response


class ClubViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=Club.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ClubSummarizeSerializer
        elif self.action == 'retrieve':
            return ClubDetailSerializer

    @action(methods=['post'], detail=True)
    def bookmark(self, request, pk):
        club = self.get_object()
        user = User.objects.filter(uuid=request.user.uuid, club_bookmarks__in=[club]).first()
        if user:
            user.club_bookmarks.remove(club)
            return Response({'message': 'delete bookmark'}, status=status.HTTP_204_NO_CONTENT)
        elif user is None:
            request.user.club_bookmarks.add(club)
            return Response({'message': 'add bookmark'}, status=status.HTTP_200_OK)
        return Response({'message': 'request data error'}, status=status.HTTP_400_BAD_REQUEST)
