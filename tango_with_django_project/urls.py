from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tango_with_django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^rango/', include('rango.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^.*$', RedirectView.as_view(url='/rango/', permanent=False), name='main'),

)
