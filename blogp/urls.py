from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^/$',views.index,name='index'),
    url(r'/post/(?P<id>\d+)',views.detial,name='detial'),
    # url(r'/post/select/(?P<page_num>\d+)',views.detial_select,name='detial_select'),
    url(r'^/archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^/category/(?P<id>\d+)/$', views.category, name='category'),
]