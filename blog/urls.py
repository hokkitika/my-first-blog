from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^data/(?P<year>[0-9]{4})-(?P<month>[01][0-9])-(?P<day>[0-3][0-9])/$', views.post_from),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^search/$', views.search, name='search'),
]