from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your login views here.

def get_login_page(request, **kwargs):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/mycraze/user-resume')
	else:
		return render(request, 'mycraze/sign-up.html')

@login_required
def get_profile_completion_page(request):
	return render(request, 'mycraze/profile-complete.html')

def get_logout_page(request):
	logout(request)
	return render(request, 'mycraze/sign-up.html')