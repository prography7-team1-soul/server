from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema, no_body
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from accounts.models import User
from accounts.permissions import IsAuthenticated
from accounts.serializer import UserSerializer


class UserDetailViewSet(mixins.RetrieveModelMixin, GenericViewSet):
    """
    유저 개인 조회 API

    ---
    """

    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    @swagger_auto_schema(operation_summary="회원가입 API", request_body=no_body,
                         operation_description="- 유저 생성을 위해 헤더에 uuid가 반드시 필요합니다. 없을 경우 {400: 잘못된 요청} 에러가 발생합니다.",
                         manual_parameters=[
                             openapi.Parameter('uuid', openapi.IN_HEADER, description="인증을 위해 반드시 헤더에 필요합니다.",
                                               type=openapi.TYPE_STRING),
                             openapi.Parameter('signup', openapi.IN_PATH, description="반드시 signup이 path에 들어가야 합니다.",
                                               type=openapi.TYPE_STRING)
                         ])
    @action(methods=['post'], detail=False)
    def signup(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        res = serializer.create(serializer.data)
        if res == 'save_fcm_token':
            response = {
                'message': 'fcm_token 변경'
            }
        else:
            response = {
                "message": "유저 생성 성공",
            }
        return Response(response)

    @swagger_auto_schema(operation_summary="유저 개인 북마크 조회 API",
                         operation_description="- query 값이 없을 경우 북마크 데이터는 주어지지 않습니다. 없이 요청하여도 성공적으로 응답됩니다. "
                                               "다만 No parameter 메세지만 전달됩니다.\n"
                                               "- 인증을 위해 uuid가 헤더에 반드시 필요하며, 없을 경우 {401: 인증 실패} 에러가 발생합니다.",
                         request_body=no_body,
                         manual_parameters=[
                             openapi.Parameter('uuid', openapi.IN_HEADER, description="인증을 위해 반드시 헤더에 필요합니다.",
                                               type=openapi.TYPE_STRING),
                             openapi.Parameter('bookmarks', openapi.IN_QUERY,
                                               description="url path에 bookmarks가 반드시 들어가야 합니다.",
                                               type=openapi.TYPE_STRING),
                             openapi.Parameter('app name', openapi.IN_QUERY, description="어떤 앱에 대한 북마크인지 반드시 query 형태로 필요합니다.",
                                                type=openapi.TYPE_STRING)
                         ])
    @action(methods=['get'], detail=True)
    def bookmarks(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        key = request.query_params.get('app', None)
        apps = ['article', 'club', 'chatroom', 'link']
        if key not in apps:
            response = {
                'message': 'Bad Request',
            }
            return Response(response, status=400)
        else:
            if key == 'club':
                data = serializer.data.get('club_data')
            elif key == 'chatroom':
                data = serializer.data.get('chatroom_data')
            elif key == 'article':
                data = serializer.data.get('article_data')
            elif key == 'link':
                data = serializer.data.get('link_data')

            response = {
                key+'_bookmark_list': data,
            }

            return Response(response)
