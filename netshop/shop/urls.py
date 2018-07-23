# -*- coding: utf-8 -*-
from __future__ import absolute_import
from django.conf.urls import url
from shop import views
from shop.views import ShopCreateView, ShopUpdateView, TypeUpdateView, TypeCreateView



urlpatterns = [
  url(r'^shop/$', views.shop, name='shop'),
  url(r'^shop/(?P<shop_id>\d+)$', views.shop_detail, name='shop_detail'),
  url(r'^type/$', views.type, name='type'),
  url(r'^type/(?P<type_id>\d+)$', views.type_detail, name='type_detail'),
  url(r'^shop/(?P<pk>\d+)/edit$', ShopUpdateView.as_view(), name='shop_edit'),
  url(r'^shop/add$', ShopCreateView.as_view(), name='shop_add'),
  url(r'^type/(?P<pk>\d+)/edit$', TypeUpdateView.as_view(), name='type_edit'),
  url(r'^type/add$', TypeCreateView.as_view(), name='type_add'),
  # url(r'^shop/add$', CustomShopCreateView.as_view(), name='shop_add'),

]