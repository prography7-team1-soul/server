from django.urls import path, include
from rest_framework.routers import SimpleRouter

from links.views import LinkViewSet

link_router = SimpleRouter(trailing_slash=False)
link_router.register('', LinkViewSet, basename='link')

urlpatterns = [
    path('links', include(link_router.urls)),

]
