from django.shortcuts import render
from rest_framework import viewsets

from club.models import Club
from club.serializers import ClubSummarizeSerializer
from rest_framework.decorators import action

from club.serializers import ClubDetailSerializer

from chat_rooms.models import ChatRoom


class ClubViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=ChatRoom.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ClubSummarizeSerializer
        elif self.action == 'retrieve':
            return ClubDetailSerializer

    @action(methods=['post'],detail=True)
    def bookmark(self, request, pk):
        pass