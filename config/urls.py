"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, re_path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.conf.urls.static import static
from config.settings import base

schema_view = get_schema_view(
    openapi.Info(
        title="SOUL API",
        default_version='v1',
        description=
        """
        SOUL API 문서 페이지입니다.
        """,
    ),
    validators=['flex'],
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('club.urls')),
    path('api/', include('accounts.urls')),
    path('api/', include('articles.urls')),
    path('api/', include('chat_rooms.urls')),
    path('api/', include('notifications.urls')),
    path('api/', include('educations.urls')),
    path('api/', include('search.urls')),
    path('api/', include('links.urls')),
]

urlpatterns += [
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(r'^swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
