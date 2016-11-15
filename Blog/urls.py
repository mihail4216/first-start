from django.conf.urls import url,include,patterns
from Blog.views import login
from django.contrib import admin
import Blog


urlpatterns = patterns('',
    url(r'^$','Blog.views.base',name='base'),
    url(r'^home/','Blog.views.home',name='home'),
    url(r'^register/','Blog.views.register',name='register'),
    url(r'^login/','Blog.views.login',name='login'),
    url(r'^logout/', 'Blog.views.logout', name='logout'),
   # url(r'^/index$', 'Blog.views.index', name='index'),
    # ex: /polls/5/
   # url(r'^(?P<question_id>[0-9]+)/$', 'Blog.views.detail', name='detail'),
    # ex: /polls/5/results/
   # url(r'^(?P<question_id>[0-9]+)/results/$',' Blog.views.results', name='results'),
    # ex: /polls/5/vote/
   # url(r'^(?P<question_id>[0-9]+)/vote/$', 'Blog.views.vote', name='vote'),
)
