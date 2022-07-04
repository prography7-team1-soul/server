from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema, no_body
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from links.models import Link
from links.serializer import LinkSerializer


class LinkViewSet(ReadOnlyModelViewSet):
    serializer_class = LinkSerializer
    queryset = Link.objects.all()

    @swagger_auto_schema(operation_summary="링크 리스트 API",
                         operation_description="- 응답을 위해 필요한 값이 없습니다. \n - 사용자의 인증이 필요하지 않습니다. \n - POST 요청이 불가능합니다.",
                         request_body=no_body)
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response = {
            'link_list': response.data,
        }
        return Response(response)

    @swagger_auto_schema(operation_summary="링크 상세보기 API",
                         operation_description="- 상세보기를 위한 데이터의 pk값이 url path에 필요합니다. \n "
                                               "- 사용자의 인증이 필요하지 않습니다. \n - POST 요청이 불가능합니다.",
                         request_body=no_body)
    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        response = {
            'link_retrieve': response.data,
        }
        return Response(response)

    @swagger_auto_schema(operation_summary="링크 북마크 등록 및 해제 API",
                         operation_description="- 상세보기를 위한 데이터의 pk값이 url path에 필요합니다. \n "
                                               "- 헤더에 uuid가 없을 경우 인증이 진행되지 않아 {401: 인증 실패} 에러가 발생합니다."
                                               "\n - GET 요청이 불가능합니다.",
                         manual_parameters=[
                             openapi.Parameter('uuid', openapi.IN_HEADER, description="인증을 위해 반드시 헤더에 필요합니다.",
                                               type=openapi.TYPE_STRING),
                             openapi.Parameter('bookmark', openapi.IN_PATH, description="반드시 bookmarks가 path에 들어가야 합니다.",
                                               type=openapi.TYPE_STRING)],
                         request_body=no_body)
    @action(methods=['POST'], detail=True)
    def bookmarks(self, request, *args, **kwargs):
        user = request.user
        if user is None:
            return Response('인증되지 않은 사용자입니다.', status=401)
        instance = Link.objects.get(pk=self.kwargs['pk'])
        if instance in user.link_bookmarks.all():
            user.link_bookmarks.remove(instance)
            user.save()
            response = {
                'message': '북마크 해제',
            }
            return Response(response, status=201)
        else:
            user.link_bookmarks.add(instance)
            user.save()
            response = {
                'message': '북마크 등록',
            }
            return Response(response, status=201)