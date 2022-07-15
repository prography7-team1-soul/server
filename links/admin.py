from django.contrib import admin

# Register your models here.
from links.models import Link, Category, SourceField

admin.site.register(Link)
admin.site.register(Category)
admin.site.register(SourceField)