from django.contrib.auth.models import User
from django.db import models

def get_upload_path(instance, filename):
    return 'profile_image/%s/%s' % (instance.user.id, filename)

class UserProfile(models.Model):
	class Meta:
		app_label = 'mycraze'

	user = models.OneToOneField(User, related_name='userProfile')
	description = models.CharField(max_length=200)
	profile_image = models.ImageField(upload_to=get_upload_path)