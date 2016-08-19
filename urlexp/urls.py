from django.conf.urls import url, patterns
from . import views
from django.contrib.auth import views as auth_views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
	url(r'^$', views.url_list, name='url_list'),
	url(r'^urlexp/$', views.url_list, name='url_list'),
	url(r'^urlitem/$', views.url_list, name='url_item'),
	url(r'^urlinfo/(?P<pk>\d+)/$', views.info_detail, name='info_detail'),
	url(r'^urldel/(?P<pk>\d+)/$', views.delete_url, name='delete_url'),
	url(r'^accounts/login/$', auth_views.login),
	url(r'^logout/$', views.logout_view, name='logout_view'),
	url(r'^logout/listret/$', views.after_logout, name='afterlogout'),
	url(r'^api/$', views.api_list),
	url(r'^api/(?P<pk>[0-9]+)/$', views.api_detail),
]