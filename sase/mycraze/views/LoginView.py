from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from mycraze.models.form.profile import UserForm
from mycraze.models.form.profile import UserProfileForm
from mycraze.models.user.profile import UserProfile
from mycraze.services.user import UserProfileService

# Create your login views here.

def get_login_page(request, **kwargs):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/mycraze/user-resume')
	else:
		return render(request, 'mycraze/sign-up.html')

@login_required
def get_profile_completion_page(request):
	data = {'first_name': request.user.first_name,
		    'last_name': request.user.last_name}
	userForm = UserForm(data)
	profileForm = UserProfileForm()
	return render(request, 'mycraze/profile-complete.html',{
        "userForm": userForm,
        "profileForm": profileForm,
    })

def submit_profile(request):
	userForm = UserForm(request.POST)
	userProfileForm = UserProfileForm(request.POST, request.FILES)
	print(request.FILES)
	if userForm.is_valid() and userProfileForm.is_valid():
		user = userForm.save(commit=False)
		userProfile = userProfileForm.save(commit=False)
		UserProfileService.save_user_profile(request.user, user, userProfile)
	return HttpResponseRedirect('/mycraze/user-resume')

def get_logout_page(request):
	logout(request)
	return HttpResponseRedirect('/mycraze/login')
