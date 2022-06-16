from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from accounts.models import User
from accounts.permissions import IsAuthenticated
from accounts.serializer import UserSerializer, UserClubBookmarkSerializer, \
    UserChatroomBookmarkSerializer, UserArticleBookmarkSerializer, UserMessageSerializer
from accounts.filters import BookmarkFilter


class UserDetailViewSet(mixins.RetrieveModelMixin, GenericViewSet):
    """
    유저 개인 page를 조회하는 API + 유저 회원가입 API

    ---
    ## `/api/users/<pk>`
    ## `/api/users/signup`
    ## 요청 메소드
        - GET 메소드만 가능합니다.
    ## 에러 메시지
        - 인증된 유저가 아닐 경우 401 Unauthorized 에러가 발생합니다.
    ## 내용
        - uuid : 유저 개인 uuid 값
        - nickname : 유저 개인 nickname
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    @action(methods=['post'], detail=False)
    def signup(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        serializer.create(serializer.data)
        response = {
            "message": "유저 생성 성공",
        }
        return Response(response)


class UserBookmarkViewSet(mixins.ListModelMixin, GenericViewSet):
    """
    유저 북마크 조회 page 생성 API

    ---
    ## `api/users/<user_pk>/bookmarks?app=<app_name>`
        - parameter로 article, chatroom, club 전달 시 각각의 북마크 리스트가 전달됩니다.
        - parameter가 전달되지 않으면 모든 앱의 북마크 리스트가 전달됩니다.
    ## 요청 메소드
        - GET 메소드만 가능합니다.
    ## 에러 메시지
        - 비인증 유저에 대해서 401 Unauthorized 에러가 발생합니다.
    ## 내용
        - article_bookmarks: 소울 후기 북마크 리스트
        - chatroom_bookmarks: 오픈톡방 북마크 리스트
        - club_bookmarks: 동아리 북마크 리스트
    """
    permission_classes = [IsAuthenticated]
    filter_backends = [BookmarkFilter]

    def get_serializer_class(self):
        if self.request.query_params.get('app') == 'club':
            return UserClubBookmarkSerializer
        elif self.request.query_params.get('app') == 'chatroom':
            return UserChatroomBookmarkSerializer
        elif self.request.query_params.get('app') == 'article':
            return UserArticleBookmarkSerializer
        else:
            return UserMessageSerializer

    def get_queryset(self):
        return User.objects.filter(pk=self.kwargs['user_pk'])

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        key = request.query_params.get('app', None)
        if key is None:
            response = {
                'message': "No parameter",
            }
        else:
            response = {
                key+'_bookmark_list': response.data,
            }
        return Response(response)



