from rest_framework.authentication import BaseAuthentication

from accounts.models import User


class UuidAuthentication(BaseAuthentication):
    def authenticate(self, request):
        if (
                request.path != "/users"
                and "admin" not in request.path
                and "swagger" not in request.path
        ):
            uuid = request.headers.get("uuid", None)

            if uuid is None:
                return None

            user = User.objects.get(uuid=uuid)
            return (user, None)
        pass
