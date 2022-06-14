from django.urls import path, include
from rest_framework.routers import SimpleRouter
from accounts.views import UserDetailViewSet, SignUpViewSet

user_router = SimpleRouter(trailing_slash=False)
user_router.register('users', UserDetailViewSet, basename='User')

user_signup_router = SimpleRouter(trailing_slash=False)
user_signup_router.register('signup', SignUpViewSet, basename='Sign up')

urlpatterns = [
    path('users/<int:pk>', include(user_router.urls)),
    path('users/', include(user_signup_router.urls)),
]
