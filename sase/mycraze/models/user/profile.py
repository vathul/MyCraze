from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.db import models
from sase.settings import PROFILE_IMAGES_DIR

fs = FileSystemStorage(location=PROFILE_IMAGES_DIR)

def get_upload_path(instance, filename):
    return 'profile_images/%s/%s' % (instance.user.id, filename)

class UserProfile(models.Model):
	class Meta:
		app_label = 'mycraze'

	user = models.OneToOneField(User, related_name='userProfile')
	description = models.CharField(max_length=200)
	profile_image = models.ImageField(upload_to=get_upload_path, storage=fs)