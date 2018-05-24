# -*- coding: utf-8 -*-
"""
Created on Fri May 18 20:12:39 2018

@author: Yogesh
"""



from django.urls import path
from crypto import views
from django.contrib.auth.views import login

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', login, {'template_name': 'crypto/login.html'}),
]
"""
urlpatterns = [
    path('', views.index, name='index'),
]


from django.conf.urls import patterns, path
from crypto import views

urlpatterns = patterns('crypto.views',
path(r'^$', 'index', name='index'), 
)"""