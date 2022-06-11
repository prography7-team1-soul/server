from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from accounts.models import User
from accounts.serializer import UserSerializer


class UserDetailViewSet(ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(uuid=self.request.user).first()


