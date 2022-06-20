from rest_framework.permissions import BasePermission

from accounts.models import User


class IsAuthenticated(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user
