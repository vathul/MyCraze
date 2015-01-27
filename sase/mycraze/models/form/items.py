from django import forms
from django.forms import ModelForm
from mycraze.models.user.items import ExperienceItem
from mycraze.models.user.items import ProjectItem

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