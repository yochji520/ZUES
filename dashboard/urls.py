#!/usr/bin/python3
#-*- coding: UTF-8 -*- 
#@Author:
#@Time:

from django.urls import path
from dashboard import views


urlpatterns = [
    path(r'', views.index_view,),
    path('welcome/', views.dashboard_view, name='welcome'),
]

