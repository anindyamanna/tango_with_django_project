from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tango_with_django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'rango.views.index', name='index'),
    url(r'^about/', 'rango.views.about', name='about'),
    url(r'^add_category/$', 'rango.views.add_category', name='add_category'),
    url(r'^category/(?P<category_name_url>\w+)/add_page/$', 'rango.views.add_page', name='add_page'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', 'rango.views.category', name='category'),
    #url(r'^register/$', 'rango.views.register', name='register'),
    #url(r'^login/$', 'rango.views.user_login', name='login'),
    url(r'^restricted/', 'rango.views.restricted', name='restricted'),
    #url(r'^logout/$', 'rango.views.user_logout', name='logout'),

)
