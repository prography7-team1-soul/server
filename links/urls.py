from django.urls import path, include
from rest_framework.routers import SimpleRouter

from links.views import LinkViewSet

link_router = SimpleRouter(trailing_slash=False)
link_router.register('links', LinkViewSet, basename='link')

urlpatterns = [
    path('', include(link_router.urls)),
]
