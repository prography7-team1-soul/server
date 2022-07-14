from django.contrib import admin

# Register your models here.
from links.models import Link, Category, Source

admin.site.register(Link)
admin.site.register(Category)
admin.site.register(Source)