from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^urlexp/$', views.url_list, name='url_list'),
	url(r'^urlitem/$', views.url_list, name='url_item'),
	url(r'^urlinfo/(?P<pk>\d+)/$', views.info_detail, name='info_detail'),
	url(r'^urldel/(?P<pk>\d+)/$', views.delete_url, name='delete_url'),
]