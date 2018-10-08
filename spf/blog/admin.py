from django.contrib import admin
from .models import Article
from .models import Tag
from .models import Photo
from .models import ArticleTag

# Register your models here.
admin.site.register(Article)
admin.site.register(Tag)
admin.site.register(Photo)
admin.site.register(ArticleTag)
