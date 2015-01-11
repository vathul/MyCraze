from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from mycraze.models.form.profile import UserForm
from mycraze.models.form.profile import UserProfileForm
from mycraze.models.user.profile import UserProfile
from mycraze.services.user import UserProfileService
# Create your views here.

@login_required
def submit_profile(request):
	userForm = UserForm(request.POST)
	userProfileForm = UserProfileForm(request.POST, request.FILES)
	print(request.FILES)
	if userForm.is_valid() and userProfileForm.is_valid():
		user = userForm.save(commit=False)
		userProfile = userProfileForm.save(commit=False)
		UserProfileService.save_user_profile(request.user, user, userProfile)
	return HttpResponseRedirect('/mycraze/user-resume')

@login_required
def get_resume_page(request):
	setting = {
		'image_url': settings.PROFILE_IMAGES_URL,
	}
	print(setting['image_url'])
	return render(request, 'mycraze/user-resume.html',setting)