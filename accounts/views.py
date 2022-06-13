from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from accounts.models import User
from accounts.serializer import UserSerializer, UserSignUpSerializer, UserBookmarkSerializer


class UserDetailViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class SignUpViewSet(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = UserSignUpSerializer
    queryset = User.objects.all()


class UserBookmarkViewSet(ModelViewSet):
    serializer_class = UserBookmarkSerializer

    def get_queryset(self):
        return User.objects.filter(uuid=self.request.user).only('club_bookmarks', 'chatroom_bookmarks', 'article_bookmarks')

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response = {
            'bookmarks_list': response.data
        }
        return Response(response)
