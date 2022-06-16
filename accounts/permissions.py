from rest_framework.permissions import BasePermission

from accounts.models import User


class IsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        if 'user_pk' in view.kwargs:
            pk = view.kwargs.get('user_pk')
        else:
            pk = view.kwargs.get('pk')
        return request.user == User.objects.get(pk=pk)
