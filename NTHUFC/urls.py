from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'NTHUFC.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('index.urls', namespace='index')),
    url(r'^photos/', include('photos.urls', namespace='photos')),
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^marker/', include('LocationMarker.urls', namespace='LocationMarker')),
)
