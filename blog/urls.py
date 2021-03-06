from django.conf.urls import url, include
from . import views

urlpatterns =[
	url(r'^jquery$', views.jquery, name='jquery'),
	url(r'^$', views.index, name='index'),
	url(r'^new/$', views.post_new, name='post_new'),
	url(r'^(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
	url(r'^(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^(?P<pk>\d+)/delete/$', views.post_delete, name='post_delete'),

	url(r'^(?P<post_pk>\d+)/comment/$', views.comment_list, name='comment_list'),
	url(r'^(?P<post_pk>\d+)/comment/new/$', views.comment_new, name='comment_new'),
	url(r'^(?P<post_pk>\d+)/comment/(?P<pk>\d+)/edit/$', views.comment_edit, name='comment_edit'),
	url(r'^(?P<post_pk>\d+)/comment/(?P<pk>\d+)/delete/$', views.comment_delete, name='comment_delete'),

	url(r'^posts\.json$', views.post_list_json),

	url(r'^api/v1/', include('blog.api')),
]