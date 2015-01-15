from django.conf.urls import patterns, include, url
from django.contrib import admin
from home import views
from auths import views
from blogs import views

admin.autodiscover()


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'demoproject.views.home', name='home'),
    # url(r'^demoproject/', include('demoproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
     url(r'^$', 'blogs.views.index'),
     url(r'^login/', 'auths.views.login'),
     url(r'^register/', 'auths.views.register'),
     url(r'^logout/', 'auths.views.logout'),
    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     url(r'^accounts/', include('registration.backends.default.urls')),
     url(r'^blogs/', include('blogs.urls')),
     url(r'^news/', 'demoproject.views.news'),
     url(r'^contact/', 'demoproject.views.contact'),
     url(r'^ckeditor/', include('ckeditor.urls')),

)
