from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from mycraze.models.user.profile import UserProfile

class UserForm(ModelForm):
	class Meta:
		model = User
		fields = ['first_name', 'last_name']
		widgets = {
			'first_name': forms.TextInput(attrs={'class': 'form-control'}),
			'last_name': forms.TextInput(attrs={'class': 'form-control'}),
		}
        
class UserProfileForm(ModelForm):
	class Meta:
		model = UserProfile
		fields = ['description','profile_image']
		widgets = {
			'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
		}
