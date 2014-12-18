from django.conf.urls import patterns, url

from mycraze.views import TemplateView
from mycraze.views import LoginView

urlpatterns = patterns('',
	#url(r'^$', views.index, name='index'),
	url(r'^template/$', TemplateView.get_template_page, name='template'),
	url(r'^login/$', LoginView.get_login_page, name='login'),
)
