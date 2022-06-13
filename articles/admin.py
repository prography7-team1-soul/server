from django.contrib import admin
from articles.models import Article, Author, Company, Part

admin.site.register(Article)
admin.site.register(Author)
admin.site.register(Company)
admin.site.register(Part)
