from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from mycraze.models.form.profile import UserForm
from mycraze.models.form.profile import UserProfileForm


# Create your login views here.
def get_login_page(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/mycraze/user-resume')
    else:
        return render(request, 'mycraze/sign-up.html')

@login_required
def get_profile_completion_page(request):
    data = {'first_name': request.user.first_name,
            'last_name': request.user.last_name}
    user_form = UserForm(data)
    profile_form = UserProfileForm()
    return render(request, 'mycraze/profile-complete.html', {
        "userForm": user_form,
        "profileForm": profile_form,
    })

def get_logout_page(request):
    logout(request)
    return HttpResponseRedirect('/mycraze/login')
