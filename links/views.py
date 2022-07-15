from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema, no_body
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from links.models import Link, Category
from links.serializer import LinkSerializer


class LinkViewSet(mixins.ListModelMixin, GenericViewSet):
    serializer_class = LinkSerializer

    def get_queryset(self):
        category = self.request.query_params.get('category', None)
        if category == None:
            return Category.objects.all()
        else:
            return Category.objects.filter(name=category)

    @swagger_auto_schema(operation_summary="링크 API",
                         operation_description="- category 파라미터로 앱 이름 전달해주세용 없으면 전체 링크 리스트 API가 나옵니당\n "
                                               "- uuid 필요 없어용",
                         request_body=no_body)
    def list(self, request, *args, **kwargs):
        response = super().list(self, request, *args, **kwargs)
        response = {
            'links_list': response.data,
        }
        return Response(response)

    @swagger_auto_schema(operation_summary="링크 북마크 등록 및 해제 API",
                         operation_description="헤더에 반드시 uuid 넣어주세요! pk는 링크 개체에 대한 pk 입니당",
                         manual_parameters=[
                             openapi.Parameter('uuid', openapi.IN_HEADER, description="인증을 위해 반드시 헤더에 필요합니다.",
                                               type=openapi.TYPE_STRING, required=True)],
                         request_body=no_body)
    @action(methods=['POST'], detail=True)
    def bookmarks(self, request, *args, **kwargs):
        user = request.user
        if user.is_anonymous:
            return Response('인증되지 않은 사용자입니다.', status=403)
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
