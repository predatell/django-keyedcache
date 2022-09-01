"""
URLConf for Caching app
"""
from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.stats_page, {}, 'keyedcache_stats'),
    re_path(r'^view/$', views.view_page, {}, 'keyedcache_view'),
    re_path(r'^delete/$', views.delete_page, {}, 'keyedcache_delete'),
]