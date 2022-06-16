from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet, ReadOnlyModelViewSet
from accounts.models import User
from accounts.permissions import IsAuthenticated
from accounts.serializer import UserSerializer, UserSignUpSerializer, UserClubBookmarkSerializer, \
    UserChatroomBookmarkSerializer, UserArticleBookmarkSerializer
from accounts.filters import BookmarkFilter


class UserDetailViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class SignUpViewSet(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = UserSignUpSerializer
    queryset = User.objects.all()


class UserBookmarkViewSet(ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    filter_backends = [BookmarkFilter]

    def get_serializer_class(self):
        if self.request.query_params.get('app') == 'club':
            return UserClubBookmarkSerializer
        elif self.request.query_params.get('app') == 'chatroom':
            return UserChatroomBookmarkSerializer
        elif self.request.query_params.get('app') == 'article':
            return UserArticleBookmarkSerializer

    def get_queryset(self):
        return User.objects.filter(pk=self.kwargs['user_pk'])

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        key = request.query_params['app']
        response = {
            key+'_bookmark_list': response.data,
        }
        return Response(response)



