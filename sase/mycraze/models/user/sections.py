"""This module contains classes pertaining to the user's section is his resume.
All these classes have one-to-one relationship with UserProfile class."""

__author__ = "Srikrishnan Suresh"
__copyright__ = "Copyright 2015, MyCraze"
__version__ = "1.0.1"

from django.db import models

from mycraze.models.user.profile import UserProfile


class SummarySection(models.Model):
	"""This module is the model class that represents user's summary section
	in the resume.
    Refer py:mycraze.models.user.profile.UserProfile
    Can be accessed by user_profile.summary_section.
    """

	class Meta:
		app_label = 'mycraze'

	user_profile = models.OneToOneField(UserProfile, related_name='summary_section')
	content = models.CharField(max_length=400)
	is_active = models.BooleanField(default=True)

class ProjectSection(models.Model):
	"""This module is the model class that represents user's project section
	in the resume.
    Refer py:mycraze.models.user.profile.UserProfile
    Can be accessed by user_profile.project_section.
    """

	class Meta:
		app_label = 'mycraze'

	user_profile = models.OneToOneField(UserProfile, related_name='project_section')
	is_active = models.BooleanField(default=True)

class ExperienceSection(models.Model):
	"""This module is the model class that represents user's experience section
	in the resume.
    Refer py:mycraze.models.user.profile.UserProfile
    Can be accessed by user_profile.experience_section.
    """

	class Meta:
		app_label = 'mycraze'

	user_profile = models.OneToOneField(UserProfile, related_name='experience_section')
	is_active = models.BooleanField(default=True)

class EducationSection(models.Model):
	"""This module is the model class that represents user's education section
	in the resume.
    Refer py:mycraze.models.user.profile.UserProfile
    Can be accessed by user_profile.education_section.
    """

	class Meta:
		app_label = 'mycraze'

	user_profile = models.OneToOneField(UserProfile, related_name='education_section')
	is_active = models.BooleanField(default=True)

class ProfileSection(models.Model):
	"""This module is the model class that represents user's profile section
	in the resume.
    Refer py:mycraze.models.user.profile.UserProfile
    Can be accessed by user_profile.profile_section.
    """

	class Meta:
		app_label = 'mycraze'

	user_profile = models.OneToOneField(UserProfile, related_name='profile_section')
	is_active = models.BooleanField(default=True)

class PublicationSection(models.Model):
	"""This module is the model class that represents user's publication section
	in the resume.
    Refer py:mycraze.models.user.profile.UserProfile
    Can be accessed by user_profile.publication_section.
    """

	class Meta:
		app_label = 'mycraze'

	user_profile = models.OneToOneField(UserProfile, related_name='publication_section')
	is_active = models.BooleanField(default=True)

class CertificationSection(models.Model):
	"""This module is the model class that represents user's certification section
	in the resume.
    Refer py:mycraze.models.user.profile.UserProfile
    Can be accessed by user_profile.certification_section.
    """

	class Meta:
		app_label = 'mycraze'

	user_profile = models.OneToOneField(UserProfile, related_name='certification_section')
	is_active = models.BooleanField(default=True)

class SkillSection(models.Model):
	"""This module is the model class that represents user's skill section
	in the resume.
    Refer py:mycraze.models.user.profile.UserProfile
    Can be accessed by user_profile.skill_section.
    """

	class Meta:
		app_label = 'mycraze'

	user_profile = models.OneToOneField(UserProfile, related_name='skill_section')
	is_active = models.BooleanField(default=True)

class CourseSection(models.Model):
	"""This module is the model class that represents user's course section
	in the resume.
    Refer py:mycraze.models.user.profile.UserProfile
    Can be accessed by user_profile.course_section.
    """

	class Meta:
		app_label = 'mycraze'

	user_profile = models.OneToOneField(UserProfile, related_name='course_section')
	is_active = models.BooleanField(default=True)

class AwardSection(models.Model):
	"""This module is the model class that represents user's award section
	in the resume.
    Refer py:mycraze.models.user.profile.UserProfile
    Can be accessed by user_profile.award_section.
    """

	class Meta:
		app_label = 'mycraze'

	user_profile = models.OneToOneField(UserProfile, related_name='award_section')
	is_active = models.BooleanField(default=True)

class LanguageSection(models.Model):
	"""This module is the model class that represents user's language section
	in the resume.
    Refer py:mycraze.models.user.profile.UserProfile
    Can be accessed by user_profile.language_section.
    """

	class Meta:
		app_label = 'mycraze'

	user_profile = models.OneToOneField(UserProfile, related_name='language_section')
	is_active = models.BooleanField(default=True)

class ContactSection(models.Model):
	"""This module is the model class that represents user's contact section
	in the resume.
    Refer py:mycraze.models.user.profile.UserProfile
    Can be accessed by user_profile.contact_section.
    """

	class Meta:
		app_label = 'mycraze'

	user_profile = models.OneToOneField(UserProfile, related_name='contact_section')
	personal_email = models.CharField(max_length=40)
	phone_number = models.CharField(max_length=20)
	is_active = models.BooleanField(default=True)