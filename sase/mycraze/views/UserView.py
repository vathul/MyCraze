from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from mycraze.models.form.profile import UserForm
from mycraze.models.form.profile import UserProfileForm
from mycraze.models.user.profile import UserProfile
from mycraze.services.user import UserProfileService
from mycraze.utils.http import JsonResponse
# Create your views here.

@login_required
def submit_profile(request):
	userForm = UserForm(request.POST)
	userProfileForm = UserProfileForm(request.POST, request.FILES)
	if userForm.is_valid() and userProfileForm.is_valid():
		user = userForm.save(commit=False)
		userProfile = userProfileForm.save(commit=False)
		UserProfileService.save_user_profile(request.user, user, userProfile)
	return HttpResponseRedirect('/mycraze/user-resume')

@login_required
def edit_profile(request):
	updated_user = User(first_name = request.POST['first_name'], last_name = request.POST['last_name'])
	updated_user_profile = UserProfile(description = request.POST['description'])
	updated_user = UserProfileService.edit_user_profile(request.user, updated_user, updated_user_profile)
	print(updated_user.first_name)
	print(updated_user.last_name)
	return JsonResponse({'first_name':updated_user.first_name, 'last_name':updated_user.last_name, 'description':updated_user.userProfile.description})

@login_required
def get_resume_page(request):
	setting = {
		'image_url': settings.PROFILE_IMAGES_URL,
	}
	return render(request, 'mycraze/user-resume.html',setting)