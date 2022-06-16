from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from accounts.models import User
from accounts.permissions import IsAuthenticated
from accounts.serializer import UserSerializer


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

    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    @action(methods=['post'], detail=False)
    def signup(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        serializer.create(serializer.data)
        response = {
            "message": "유저 생성 성공",
        }
        return Response(response)

    @action(methods=['get'], detail=True)
    def bookmarks(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        key = request.query_params.get('app', None)
        if key is None:
            response = {
                'message': 'No Parameter',
            }
        else:
            if key == 'club':
                data = serializer.data.get('club_data')
            elif key == 'chatroom':
                data = serializer.data.get('chatroom_data')
            else:
                data = serializer.data.get('article_data')

            response = {
                key+'_bookmark_list': data,
            }

        return Response(response)
