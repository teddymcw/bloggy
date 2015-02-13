from django.conf.urls import patterns, include, url
from django.contrib import admin
from .settings import MEDIA_ROOT

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bloggy_project.views.home', name='home'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': MEDIA_ROOT}),
)
