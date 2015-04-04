"""This module contains classes pertaining to the forms used by the user to
add and edit various sections in the user resume page"""

__author__ = "Srikrishnan Suresh"
__copyright__ = "Copyright 2015, MyCraze"
__version__ = "1.0.1"

from django import forms
from django.forms import ModelForm

from mycraze.models.user.sections import ContactSection


class ContactSectionForm(ModelForm):
    """This module is the model class for contact section form, with which user
    adds and edits contact section in user resume
    page.
    """

    class Meta:
        """This is the meta class for the model.
        Refer py:module::mycraze.models.user.sections.ContactSection
        All fields are mandatory by design.
        """
        model = ContactSection
        fields = ['personal_email', 'phone_number']
        widgets = {
            'personal_email': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
        }
