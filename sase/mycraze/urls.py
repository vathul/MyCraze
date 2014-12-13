from django.conf.urls import patterns, url

from mycraze.views import TestView
from mycraze.views import LoginView

urlpatterns = patterns('',
	#url(r'^$', views.index, name='index'),
	url(r'^test/$', TestView.test, name='test'),
	url(r'^login/$', LoginView.get_login_page, name='login'),
)
