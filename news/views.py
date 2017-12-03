# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from models import Article, Column
from django.shortcuts import redirect


def index(request):
    # return HttpResponse(u'Welcome to my Index!')
    columns = Column.objects.all()
    return render(request, 'news/index.html', {'columns': columns})


def column_detail(request, column_slug):
    # return HttpResponse('column slug ' + column_slug)
    column = Column.objects.get(slug=column_slug)
    return render(request, 'news/column.html', {"column": column})


def article_detail(request, pk, article_slug):
    # return HttpResponse('article slug ' + article_slug)
    article = Article.objects.get(pk=pk)
    if article_slug != article.slug:
        # 在传递一个Model object时，会自动调用 object的get_absolute_url获取网址
        return redirect(article, permanent=True)
    return render(request, 'news/article.html', {"article": article})
# Create your views here.
