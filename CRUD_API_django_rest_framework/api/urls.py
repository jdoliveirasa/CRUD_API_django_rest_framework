#from django.conf.urls import patterns, url
from django.conf.urls import url
from api import views

#urlpatterns = patterns(
urlpatterns = [
    #'api.views',
    #url(r'^tasks/$', 'task_list', name='task_list'),
	url(r'^tasks/$', views.task_list, name='task_list'),
    #url(r'^tasks/(?P<pk>[0-9]+)$', 'task_detail', name='task_detail'),  
    url(r'^tasks/(?P<pk>[0-9]+)$', views.task_detail, name='task_detail'),  
]
#)