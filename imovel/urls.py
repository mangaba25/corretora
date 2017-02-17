# coding=utf-8

from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^venda/$', views.venda, name='venda'),
    url(r'^aluguel/$', views.aluguel, name='aluguel'),
    url(r'^(?P<slug>[\w_-]+)$', views.imovel, name='imovel'),
]
