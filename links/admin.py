from django.contrib import admin

# Register your models here.
from links.models import Link, Category, Source, Tag

admin.site.register(Link)
admin.site.register(Category)
admin.site.register(Source)
admin.site.register(Tag)
