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

def article_detail(request, pk):
    article = Article.objects.get(id=pk)
    # photo = Photo.objects.get(id=pk)

    return render(request, 'article_detail.html',
         {'article': article})

def tag_index(request, pk):
    articles = Article.objects.all()
    tags = Tag.objects.get(id=pk)
    return render(request, 'tag_index.html',
    {'tags':tags},
    {'articles' : articles})
    
