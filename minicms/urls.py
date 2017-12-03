# coding:utf-8
"""minicms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from DjangoUeditor import urls as editor_urls
from news import views as news_views
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ueditor/', include(editor_urls)),
    url(r'^$', news_views.index, name='index'),
    # 使用非通用匹配url，就是按文章单独分配url
    # 使用正则表达式组来进行匹配
    url(r'^column/(?P<column_slug>[^/]+)/$', news_views.column_detail, name='column'),
    # 第一版url：会出现重复的现象。
    # url(r'^news/(?P<article_slug>[^/]+)/$', news_views.article_detail, name='article'),
    # 第二版url：添加主键标志，有效去重
    url(r'^news/(?P<pk>\d+)/(?P<article_slug>[^/]+)/$', news_views.article_detail, name='article')
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
