from django.urls import path, include
from rest_framework.routers import DefaultRouter

from notifications.views import NotificationViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'notifications', NotificationViewSet, basename='notifications')

urlpatterns = [
    path("", include(router.urls)),
]