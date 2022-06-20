from django.contrib import admin
from .models import ChatRoom, Category

admin.site.register([ChatRoom, Category])