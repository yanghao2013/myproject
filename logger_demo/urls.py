# _*_ coding:utf-8 _*_

__author__ = 'yanghao'
__date__ = '2017/10/16 22:46'
from django.conf.urls import url
from .views import *

urlpatterns = [

    url(r'^log_test',logger_test,name="logger_text"),
]