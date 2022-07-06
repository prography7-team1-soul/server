from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema, no_body
from rest_framework import viewsets, status
from .models import Education
from .serializers import EducationSummarizeSerializer, EducationDetailSerializer
from rest_framework.decorators import action
from accounts.models import User
from rest_framework.response import Response


class EducationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Education.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return EducationSummarizeSerializer
        elif self.action == 'retrieve':
            return EducationDetailSerializer
        elif self.action == 'bookmark':
            return None

    @swagger_auto_schema(operation_summary="교육 리스트 API", request_body=no_body,
                         operation_description="- 헤더는 필요없어요!",)
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response = {
            'education_list': response.data
        }
        return Response(response, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_summary="교육 상세보기 API", request_body=no_body,
                         manual_parameters=[
                             openapi.Parameter('id', openapi.IN_PATH, description="반드시 url에 식별자 id값이 필요합니다.",
                                               type=openapi.TYPE_STRING)
                         ])
    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        response = {
            'education_retrieve': response.data
        }
        return Response(response, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_summary="교육 북마크 on/off API", operation_description="request header에 uuid 필수!",
                         request_body=no_body,
                         manual_parameters=[
                             openapi.Parameter('uuid', openapi.IN_HEADER, description="인증을 위해 반드시 헤더에 필요합니다.",
                                               type=openapi.TYPE_STRING),
                         ])
    @action(methods=['post'], detail=True)
    def bookmark(self, request, pk):
        education = self.get_object()
        user = User.objects.filter(uuid=request.user.uuid, education_bookmarks__in=[education]).first()
        if user:
            user.education_bookmarks.remove(education)
            return Response({'message': 'delete bookmark'}, status=status.HTTP_204_NO_CONTENT)
        elif user is None:
            request.user.education_bookmarks.add(education)
            return Response({'message': 'add bookmark'}, status=status.HTTP_200_OK)
        return Response({'message': 'request data error'}, status=status.HTTP_400_BAD_REQUEST)
