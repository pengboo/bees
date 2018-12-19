from django.shortcuts import render
from django.http import HttpResponse
from news.models import Column, Article


# Create your views here.

def column_detail(request, column_slug):
    column = Column.objects.get(slug=column_slug)
    return render(request, 'news/column.html', {'column':column})

def article_detail(request, article_slug):
    article = Article.objects.get(slug=article_slug)
    print(article)
    return render(request, 'news/article.html', {'article':article})
