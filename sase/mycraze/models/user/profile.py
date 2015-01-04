from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
	class Meta:
		app_label = 'mycraze'

	user = models.OneToOneField(User, related_name='userProfile')
	description = models.CharField(max_length=200)
	profile_image = models.ImageField(upload_to="profile_image/", null=True, blank=True)