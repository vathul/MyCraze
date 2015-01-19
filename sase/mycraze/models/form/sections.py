from django import forms
from django.forms import ModelForm
from mycraze.models.user.sections import ContactSection

class ContactSectionForm(ModelForm):
	class Meta:
		model = ContactSection
		fields = ['personal_email', 'phone_number']
		widgets = {
			'personal_email': forms.TextInput(attrs={'class': 'form-control'}),
			'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
		}