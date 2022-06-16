from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from accounts.models import User
from accounts.permissions import IsAuthenticated
from accounts.serializer import UserSerializer, UserClubBookmarkSerializer, \
    UserChatroomBookmarkSerializer, UserArticleBookmarkSerializer, UserBookmarkSerializer
from accounts.filters import BookmarkFilter


class UserDetailViewSet(mixins.RetrieveModelMixin, GenericViewSet):
    """
    유저 개인 page를 조회하는 API

    ---
    ## `/api/users/<pk>`
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


class SignUpViewSet(mixins.CreateModelMixin, GenericViewSet):
    """
    유저 회원 가입 page 생성 API

    ---
    ## `/api/signup`
    ## 요청 메소드
        - POST 메소드만 가능합니다.
    ## 에러 메시지
        - 이미 가입된 값일 경우 '이미 가입된 계정입니다' 라는 에러메시지 발생
    ## 내용
        - uuid : 유저 개인 uuid 값
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()


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
            return UserBookmarkSerializer

    def get_queryset(self):
        return User.objects.filter(pk=self.kwargs['user_pk'])

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        key = request.query_params['app']
        if key is None:
            response = {
                'all_bookmark_list': response.data,
            }
        else:
            response = {
                key+'_bookmark_list': response.data,
            }
        return Response(response)



