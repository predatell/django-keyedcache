"""
URLConf for Caching app
"""

from . import views

urlpatterns = [
    (r'^$', views.stats_page, {}, 'keyedcache_stats'),
    (r'^view/$', views.view_page, {}, 'keyedcache_view'),
    (r'^delete/$', views.delete_page, {}, 'keyedcache_delete'),
]