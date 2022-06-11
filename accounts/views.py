from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from accounts.models import User
from accounts.serializer import UserSerializer, UserSignUpSerializer


class UserDetailViewSet(ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(uuid=self.request.user).first()


class SignUpViewSet(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = UserSignUpSerializer
    queryset = User.objects.all()
