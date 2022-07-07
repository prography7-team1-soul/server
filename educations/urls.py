from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import EducationViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'educations', EducationViewSet, basename='education')

urlpatterns = [
    path("", include(router.urls)),
]