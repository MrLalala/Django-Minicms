# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from DjangoUeditor.models import UEditorField
from django.core.urlresolvers import reverse


@python_2_unicode_compatible
class Column(models.Model):
    # db_index = True:意味着建立索引
    name = models.CharField('栏目名称', max_length=256)
    slug = models.CharField('栏目网址', max_length=256, db_index=True)
    intro = models.TextField('栏目简介', default='')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('column', args=(self.slug, ))

    class Meta:
        # 貌似就是看起来更方便的东西。
        verbose_name = '栏目'
        verbose_name_plural = '栏目'
        # 指定数据库中的表的名字
        '''db_table = 'column' '''
        # Ordering by Name
        ordering = ['name']


@python_2_unicode_compatible
class Article(models.Model):
    # 在一对一、多对多、外键等关系中，verbose_name这一选项可选。。
    # 事实是：加不加verbose_name对数据层面没有影响。
    # 添加verbose_name会将类型变成该名字。
    column = models.ManyToManyField(Column, verbose_name='归属栏目')

    title = models.CharField('标题', max_length=256)
    slug = models.CharField('网址', max_length=256, db_index=True)

    author = models.ForeignKey('auth.User', blank=True, null=True, verbose_name='作者')
    content = UEditorField('内容', height=300, width=1000,
                           default=u'', blank=True, imagePath='uploads/images/',
                           toolbars='besttome', filePath='upload/files/')

    published = models.BooleanField('正式发布', default=True)
    pub_date = models.DateTimeField('发表时间', auto_now_add=True, editable=True)
    update_date = models.DateTimeField('更新时间', auto_now=True, null=True)

    def __str__(self):
        return self.title

    # 获得绝对地址的方式
    def get_absolute_url(self):
        return reverse('article', args=(self.slug, ))

    class Meta:
        verbose_name = '教程'
        verbose_name_plural = '教程'
# Create your models here.
