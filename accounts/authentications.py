from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication

from accounts.models import User


class UuidAuthentication(BaseAuthentication):
    def authenticate(self, request):
        if (
                request.path != "/api/users/signup"
                and "admin" not in request.path
                and "swagger" not in request.path
        ):
            uuid = request.headers.get("uuid", None)

            if uuid is None:
                return None
            try:
                user = User.objects.get(uuid=uuid)
            except User.DoesNotExist:
                raise exceptions.AuthenticationFailed('No Such user')
            return (user, None)
        pass
