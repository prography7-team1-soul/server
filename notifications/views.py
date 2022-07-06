from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema, no_body
from rest_framework import viewsets, mixins, status

from notifications.models import Notification

from notifications.serializers import NotificationSerializer, NotificationIsReadSerializer
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet


class NotificationViewSet(mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.ListModelMixin,
                          GenericViewSet):

    def get_queryset(self):
        user = self.request.user
        return Notification.objects.filter(user=user)

    def get_serializer_class(self):
        if self.action == 'update':
            return NotificationIsReadSerializer
        else:
            return NotificationSerializer

    @swagger_auto_schema(operation_summary="알림 리스트 API", operation_description="request header에 uuid 필수!",
                         request_body=no_body,
                         manual_parameters=[
                             openapi.Parameter('uuid', openapi.IN_HEADER, description="인증을 위해 반드시 헤더에 필요합니다.",
                                               type=openapi.TYPE_STRING),
                         ])
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response = {
            'notification_list': response.data
        }
        return Response(response, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_summary="알림 상세보기 API", operation_description="request header에 uuid 필수!",
                         request_body=no_body,
                         manual_parameters=[
                             openapi.Parameter('uuid', openapi.IN_HEADER, description="인증을 위해 반드시 헤더에 필요합니다.",
                                               type=openapi.TYPE_STRING),
                             openapi.Parameter('id', openapi.IN_PATH, description="반드시 url에 식별자 id값이 필요합니다.",
                                               type=openapi.TYPE_STRING)
                         ])
    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        response = {
            'notification_retrieve': response.data
        }
        return Response(response, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_summary="읽은 알림 수정 API", operation_description="request header에 uuid 필수!",
                         manual_parameters=[
                             openapi.Parameter('uuid', openapi.IN_HEADER, description="인증을 위해 반드시 헤더에 필요합니다.",
                                               type=openapi.TYPE_STRING),
                             openapi.Parameter('id', openapi.IN_PATH, description="반드시 url에 식별자 id값이 필요합니다.",
                                               type=openapi.TYPE_STRING)
                         ])
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        response = {
            'notification_update': response.data
        }
        return Response(response, status=status.HTTP_200_OK)