"""This module contains classes pertaining to the forms used by the user to
add and edit various items in the user resume page"""

__author__ = "Srikrishnan Suresh"
__copyright__ = "Copyright 2015, MyCraze"
__version__ = "1.0.1"

from django import forms
from django.forms import ModelForm

from mycraze.models.user.items import AwardItem
from mycraze.models.user.items import CertificationItem
from mycraze.models.user.items import CourseItem
from mycraze.models.user.items import EducationItem
from mycraze.models.user.items import ExperienceItem
from mycraze.models.user.items import LanguageItem
from mycraze.models.user.items import ProjectItem
from mycraze.models.user.items import PublicationItem
from mycraze.models.user.items import SkillItem

class ExperienceItemForm(ModelForm):
    """This module is the model class for experience item form, with which user
    adds and edits an experience item under the experience section in user resume
    page.
    """

    class Meta:
        """This is the meta class for the model.
        Refer py:module:: mycraze.models.user.items.ExperienceItem
        All fields are mandatory by design.
        """
        model = ExperienceItem
        fields = ['role', 'organization', 'description']
        widgets = {
            'role': forms.TextInput(attrs={'class': 'form-control'}),
            'organization': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }

class ProjectItemForm(ModelForm):
    """This module is the model class for project item form, with which user
	adds and edits an project item under the project section in user resume
	page.
	"""

    class Meta:
        """This is the meta class for the model.
        Refer py:module:: mycraze.models.user.items.ProjectItem
        All fields are mandatory by design.
        """
        model = ProjectItem
        fields = ['title', 'url', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'url': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }

class EducationItemForm(ModelForm):
    """This module is the model class for education item form, with which user
	adds and edits an project item under the education section in user resume
	page.
	"""

    class Meta:
        """This is the meta class for the model.
        Refer py:module:: mycraze.models.user.items.EducationItem
        All fields are mandatory by design.
        """
        model = EducationItem
        fields = ['school', 'degree', 'description']
        widgets = {
            'school': forms.TextInput(attrs={'class': 'form-control'}),
            'degree': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }

class PublicationItemForm(ModelForm):
    """This module is the model class for publication item form, with which user
	adds and edits an publication item under the publication section in user resume
	page.
	"""

    class Meta:
        """This is the meta class for the model.
        Refer py:module:: mycraze.models.user.items.PublicationItem
        All fields are mandatory by design.
        """
        model = PublicationItem
        fields = ['title', 'publisher', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'publisher': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }

class CertificationItemForm(ModelForm):
    """This module is the model class for certification item form, with which user
	adds and edits an certification item under the certification section in user resume
	page.
	"""

    class Meta:
        """This is the meta class for the model.
        Refer py:module:: mycraze.models.user.items.CertificationItem
        All fields are mandatory by design.
        """
        model = CertificationItem
        fields = ['title', 'certifier']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'certifier': forms.TextInput(attrs={'class': 'form-control'})
        }

class SkillItemForm(ModelForm):
    """This module is the model class for skill item form, with which user
	adds and edits an skill item under the skill section in user resume
	page.
	"""

    class Meta:
        """This is the meta class for the model.
        Refer py:module:: mycraze.models.user.items.SkillItem
        All fields are mandatory by design.
        """
        model = SkillItem
        fields = ['skill']
        widgets = {
            'skill': forms.TextInput(attrs={'class': 'form-control'})
        }

class CourseItemForm(ModelForm):
    """This module is the model class for course item form, with which user
	adds and edits an course item under the course section in user resume
	page.
	"""

    class Meta:
        """This is the meta class for the model.
        Refer py:module::mycraze.models.user.items.CourseItem
        All fields are mandatory by design.
        """
        model = CourseItem
        fields = ['title', 'code']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'code': forms.TextInput(attrs={'class': 'form-control'})
        }

class AwardItemForm(ModelForm):
    """This module is the model class for award item form, with which user
	adds and edits an award item under the award section in user resume
	page.
    """

    class Meta:
        """This is the meta class for the model.
        Refer py:module::mycraze.models.user.items.AwardItem
        All fields are mandatory by design.
        """
        model = AwardItem
        fields = ['title', 'issuer', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'issuer': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }

class LanguageItemForm(ModelForm):
    """This module is the model class for language item form, with which user
	adds and edits an language item under the language section in user resume
	page.
	"""
    class Meta:
        """This is the meta class for the model.
        Refer py:module::mycraze.models.user.items.LanguageItem
        All fields are mandatory by design.
        """
        model = LanguageItem
        fields = ['language']
        widgets = {
            'language': forms.TextInput(attrs={'class': 'form-control'})
        }
