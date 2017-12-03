#coding:utf-8
from django import VERSION
from views import get_ueditor_controller
if VERSION[0:2] > (1,3):
    from django.conf.urls import url
else:
    from django.conf.urls import url

urlpatterns = [
    url(r'^controller/$', get_ueditor_controller),
]