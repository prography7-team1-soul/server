from django.urls import path, include
from rest_framework.routers import SimpleRouter
from accounts.views import UserDetailViewSet

user_router = SimpleRouter(trailing_slash=False)
user_router.register('users', UserDetailViewSet, basename='User')

url_patterns = [
    path('users/<int:pk>', include(user_router.urls)),
]
