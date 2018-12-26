from django.shortcuts import render, redirect
from django.http import HttpResponse
from news.models import Column, Article


# Create your views here.
def index(request):
    columns = Column.objects.all()
    return render(request, 'index.html', {'columns':columns})

def column_detail(request, column_slug):
    column = Column.objects.get(slug=column_slug)
    return render(request, 'news/column.html', {'column': column})


def article_detail(request, pk, article_slug):
    article = Article.objects.get(pk=pk)

    #访问的文章地址与现在的文章地址不一样时，重定向（301）跳转到新的地址
    if article_slug != article.slug:
        return redirect(article, permanent=True)

    return render(request, 'news/article.html', {'article': article})


