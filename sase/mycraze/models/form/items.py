from django import forms
from django.forms import ModelForm

from mycraze.models.user.items import CertificationItem
from mycraze.models.user.items import CourseItem
from mycraze.models.user.items import EducationItem
from mycraze.models.user.items import ExperienceItem
from mycraze.models.user.items import ProjectItem
from mycraze.models.user.items import PublicationItem
from mycraze.models.user.items import SkillItem

class ExperienceItemForm(ModelForm):
	class Meta:
		model = ExperienceItem
		fields = ['role', 'organization', 'description']
		widgets = {
			'role': forms.TextInput(attrs={'class': 'form-control'}),
			'organization': forms.TextInput(attrs={'class': 'form-control'}),
			'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
		}

class ProjectItemForm(ModelForm):
	class Meta:
		model = ProjectItem
		fields = ['title', 'url', 'description']
		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'url': forms.TextInput(attrs={'class': 'form-control'}),
			'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
		}

class EducationItemForm(ModelForm):
	class Meta:
		model = EducationItem
		fields = ['school', 'degree', 'description']
		widgets = {
			'school': forms.TextInput(attrs={'class': 'form-control'}),
			'degree': forms.TextInput(attrs={'class': 'form-control'}),
			'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
		}

class PublicationItemForm(ModelForm):
	class Meta:
		model = PublicationItem
		fields = ['title', 'publisher', 'description']
		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'publisher': forms.TextInput(attrs={'class': 'form-control'}),
			'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
		}

class CertificationItemForm(ModelForm):
	class Meta:
		model = CertificationItem
		fields = ['title', 'certifier']
		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'certifier': forms.TextInput(attrs={'class': 'form-control'})
		}

class SkillItemForm(ModelForm):
	class Meta:
		model = SkillItem
		fields = ['skill']
		widgets = {
			'skill': forms.TextInput(attrs={'class': 'form-control'})
		}

class CourseItemForm(ModelForm):
	class Meta:
		model = CourseItem
		fields = ['title', 'code']
		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'code': forms.TextInput(attrs={'class': 'form-control'})
		}		