from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from .models import Article, Tag, ArticleTag, Photo


# Create your views here.
def index(request):
    articles_list = Article.objects.all()
    page = request.GET.get('page',1)

    paginator = Paginator(articles_list, 1)
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    return render(request, 'article_list.html', 
        {'articles': articles})

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
    

