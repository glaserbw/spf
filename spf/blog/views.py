from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, Tag, ArticleTag, Photo


# Create your views here.
def index(request):
    articles = Article.objects.all()
    tags = Tag.objects.all()
    return render(request, 'article_list.html', 
        {'articles': articles},
        {'tags': tags})
