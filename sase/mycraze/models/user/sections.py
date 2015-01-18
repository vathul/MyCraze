from django.db import models
from mycraze.models.user import UserProfile

class SummarySection(models.Model):
	class Meta:
		app_label = 'mycraze'

	user_profile = models.OneToOneField(UserProfile, related_name='summary_section')
	content = models.CharField(max_length=400)
	is_active = models.BooleanField(default=True)