from django.contrib import admin
from .models import Article, Tag, Photo, ArticleTag


# Register your models here.
admin.site.register(Article)
admin.site.register(Tag)
admin.site.register(Photo)
admin.site.register(ArticleTag)
