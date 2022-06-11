from django.urls import path, include
from rest_framework.routers import DefaultRouter

from club.views import ClubViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'club', ClubViewSet, basename='club')

urlpatterns = [
    path("", include(router.urls)),
]