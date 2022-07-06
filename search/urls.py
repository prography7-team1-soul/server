from django.urls import path
from rest_framework.routers import SimpleRouter
from search.views import SearchView

search_router = SimpleRouter(trailing_slash=False)
search_router.register('', SearchView, basename='Search')

urlpatterns = [
    path('search/', SearchView.as_view()),
]
