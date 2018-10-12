from django.contrib import admin
from .models import Article, Tag, Photo, ArticleTag

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'subhead', 'pub_date')
    list_filter = ('title', 'pub_date', 'tags')

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('caption', 'photo')

class TagAdmin(admin.ModelAdmin):
    list_filter = ('articles', 'tag')

class ArticleTagAdmin(admin.ModelAdmin):
    list_display = ('tag', 'article')

admin.site.site_header = "Salt & Pepper Family Admin"
admin.site.index_title = ""

# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(ArticleTag, ArticleTagAdmin)
