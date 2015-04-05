"""This module contains view classes pertaining to login, sign up and profile
completion."""

__author__ = "Srikrishnan Suresh"
__copyright__ = "Copyright 2015, MyCraze"
__version__ = "1.0.1"

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from mycraze.models.form.profile import UserForm
from mycraze.models.form.profile import UserProfileForm

def get_login_page(request):
    """This function returns the login/sign up page view if the user is
    not authenticated yet. If an authenticated user enters, the user is
    redirected to resume page. 
    """

    if request.user.is_authenticated():
        response_url = '/mycraze/user-resume/' + str(request.user.id)
        return HttpResponseRedirect(response_url)
    else:
        return render(request, 'mycraze/sign-up.html')

@login_required
def get_profile_completion_page(request):
    """This function returns the profile completion page view with the form
    for the user to fill his profile information. 
    """

    data = {'first_name': request.user.first_name,
            'last_name': request.user.last_name}
    user_form = UserForm(data)
    profile_form = UserProfileForm()
    return render(request, 'mycraze/profile-complete.html', {
        "userForm": user_form,
        "profileForm": profile_form,
    })

def get_logout_page(request):
    """This function logs out the user and redirects him to logout page. The
    cookies created by Django are not cleared during logout.  
    """
    logout(request)
    return render(request, 'mycraze/logout.html')
