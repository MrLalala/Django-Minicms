# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# from django.http import HttpResponse
from models import Article, Column
from django.shortcuts import redirect


def index(request):
    # *-----自定义显示内容
    # return HttpResponse(u'Welcome to my Index!')
    # *-----显示所有栏目
    # columns = Column.objects.all()
    # 使用自定义显示模式
    home_display_columns = Column.objects.filter(home_display=True)
    nav_display_columns = Column.objects.filter(nav_display=True)
    return render(request, 'news/index.html',
                  {'home_display_columns': home_display_columns,
                   'nav_display_columns': nav_display_columns})


def column_detail(request, column_slug):
    # return HttpResponse('column slug ' + column_slug)
    column = Column.objects.get(slug=column_slug)
    return render(request, 'news/column.html', {"column": column})


def article_detail(request, pk, article_slug):
    # return HttpResponse('article slug ' + article_slug)
    article = Article.objects.get(pk=pk)
    # 当收藏夹内url和已经修改后的url不匹配，该怎么办？
    # 应当注意：不管slug怎么改，pk是固定的。所以可以通过这个特点，在slug（url）更改后
    # 使用redirect的方式进行重新匹配
    if article_slug != article.slug:
        # 在传递一个Model object时，会自动调用 object的get_absolute_url获取网址
        # 通过redirect，将连接再一次通过view进行匹配，然后返回render
        return redirect(article, permanent=True)
    return render(request, 'news/article.html', {"article": article})
# Create your views here.
