from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from mycraze.models.form.profile import UserForm
from mycraze.models.form.profile import UserProfileForm
from mycraze.models.form.sections import ContactSectionForm
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
	response_url = '/mycraze/user-resume/' + str(request.user.id)
	return HttpResponseRedirect(response_url)

@login_required
def edit_profile(request):
	updated_user = User(first_name = request.POST['first_name'], last_name = request.POST['last_name'])
	updated_user_profile = UserProfile(description = request.POST['description'])
	updated_user = UserProfileService.edit_user_profile(request.user, updated_user, updated_user_profile)
	return JsonResponse({'first_name':updated_user.first_name, 'last_name':updated_user.last_name, 'description':updated_user.user_profile.description})

@login_required
def get_resume_page(request,user_id):
	if not UserProfileService.has_user_profile(request.user):
		return HttpResponseRedirect('/mycraze/profile-complete/')
	user_id = int(user_id)
	user = get_object_or_404(User, id=user_id)
	contact_data = {'personal_email': user.user_profile.contact_section.personal_email,
		    'phone_number': user.user_profile.contact_section.phone_number}
	contact_form = ContactSectionForm(contact_data)
	stackoverflow_profile_list = user.social_auth.filter(provider='stackoverflow')
	has_edit_permission = True if request.user == user else False
	context = {
		'user': user,
		'has_edit_permission': has_edit_permission,
		'image_url': settings.PROFILE_IMAGES_URL,
		'contact_form': contact_form,
		'stackoverflow_profile_list': stackoverflow_profile_list
	}
	return render(request, 'mycraze/user-resume.html',context)

@login_required
def get_my_work_page(request,user_id):
	if not UserProfileService.has_user_profile(request.user):
		return HttpResponseRedirect('/mycraze/profile-complete/')
	user_id = int(user_id)
	user = User.objects.get(id=user_id)
	has_edit_permission = True if request.user == user else False
	context = {
		'user': user,
		'has_edit_permission': has_edit_permission,
		'image_url': settings.PROFILE_IMAGES_URL
	}
	return render(request, 'mycraze/my-work.html',context)