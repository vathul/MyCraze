"""This module contains classes pertaining to the forms used by the user to
complete his profile information and edit it later."""

__author__ = "Srikrishnan Suresh"
__copyright__ = "Copyright 2015, MyCraze"
__version__ = "1.0.1"

from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

from mycraze.models.user.profile import UserProfile


class UserForm(ModelForm):
    """This module is the model class for user form, with which user
    adds and edits his name.
    """
    class Meta:
        """This is the meta class for the model.
        Refer py:module::django.contrib.auth.models.User
        All fields are mandatory by design.
        """
        model = User
        fields = ['first_name', 'last_name']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class UserProfileForm(ModelForm):
    """This module is the model class for user profile form, which is an
    extension of the user form. This is the model for the form with which
    a user adds and edits his profile information such as description and
    profile image.
    """
    class Meta:
        """This is the meta class for the model.
        Refer py:module::mycraze.models.user.profile.UserProfile
        All fields are mandatory by design.
        """
        model = UserProfile
        fields = ['description', 'profile_image']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }
