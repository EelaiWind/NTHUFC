from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    url(r'^$', views.users, name='profile'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^delete_photo/(?P<delete_id>.*)/$', views.delete_photo),
)
