"""This module contains classes pertaining to the user's profile. This is an
extended user class (not inherited). The extended information are
description about the user and his profile image"""

__author__ = "Srikrishnan Suresh"
__copyright__ = "Copyright 2015, MyCraze"
__version__ = "1.0.1"

from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.db import models

from sase.settings import PROFILE_IMAGES_DIR


file_store = FileSystemStorage(location=PROFILE_IMAGES_DIR)

def get_upload_path(instance, filename):
    """This function returns the image path that can be rendered on the
    django template.
    """
    return 'profile_images/%s/%s' % (instance.user.id, filename)

class UserProfile(models.Model):
    """This module is the model class that extends (not inheritance, but one-to-one relationship)
    Django's user to represent user's profile.
    Refer py:module::django.contrib.auth.models.User
    Can be accessed by user.user_profile.
    """
    class Meta:
        app_label = 'mycraze'

    user = models.OneToOneField(User, related_name='user_profile', null=True)
    description = models.CharField(max_length=200)
    profile_image = models.ImageField(upload_to=get_upload_path, storage=file_store)
