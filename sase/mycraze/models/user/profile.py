from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
	class Meta:
		app_label = 'mycraze'

	user = models.OneToOneField(User)
	description = models.CharField(max_length=200)