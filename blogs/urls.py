from django.conf.urls import patterns, url

urlpatterns = patterns('blogs.views',
    url(r'^$', 'blogs'),
    url(r'^(?P<blog_id>\d+)/$', 'detail'),
    url(r'^myblogs/$', 'myblogs'),
    url(r'^create/$', 'create'),
    url(r'^edit/(?P<blog_id>\d+)/$', 'edit'),
    url(r'^delete/(?P<blog_id>\d+)/$', 'delete'),
)
