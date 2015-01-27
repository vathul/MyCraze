from django.conf.urls import patterns, url

from mycraze.views import TemplateView
from mycraze.views import LoginView
from mycraze.views import UserView
from mycraze.views import UserProfileView
from mycraze.views import UserFormView

urlpatterns = patterns('',
	#url(r'^$', views.index, name='index'),
	url(r'^template/$', TemplateView.get_template_page, name='template'),
	url(r'^login/$', LoginView.get_login_page, name='login'),
	url(r'^logout/$', LoginView.get_logout_page, name='logout'),
	url(r'^profile-complete/$', LoginView.get_profile_completion_page, name='profile_complete'),
	url(r'^submit-profile/$', UserView.submit_profile, name='submit_profile'),
	url(r'^user-resume/$', UserView.get_resume_page, name='resume'),
	url(r'^edit-profile/$', UserView.edit_profile, name='edit_profile'),
	url(r'^edit-summary/$', UserProfileView.edit_summary, name='edit_summary'),
	url(r'^edit-experience/$', UserProfileView.edit_experience, name='edit_experience'),
	url(r'^get-experience-form/$', UserFormView.get_experience_form, name='get_experience_form'),
	url(r'^edit-project/$', UserProfileView.edit_project, name='edit_project'),
	url(r'^get-project-form/$', UserFormView.get_project_form, name='get_project_form'),
	url(r'^edit-contact/$', UserProfileView.edit_contact, name='edit_contact'),
)
