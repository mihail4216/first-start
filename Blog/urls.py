from django.conf.urls import url,include,patterns
from django.contrib import admin


urlpatterns = patterns('',
    url(r'^$','Blog.views.base',name='base'),
    url(r'^home','Blog.views.home',name='home'),
    url(r'^register','Blog.views.register',name='register'),
)