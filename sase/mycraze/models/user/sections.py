from django.db import models
from mycraze.models.user.profile import UserProfile

class SummarySection(models.Model):
	class Meta:
		app_label = 'mycraze'

	user_profile = models.OneToOneField(UserProfile, related_name='summary_section')
	content = models.CharField(max_length=400)
	is_active = models.BooleanField(default=True)

class ProjectSection(models.Model):
	class Meta:
		app_label = 'mycraze'

	user_profile = models.OneToOneField(UserProfile, related_name='project_section')
	is_active = models.BooleanField(default=True)

class ExperienceSection(models.Model):
	class Meta:
		app_label = 'mycraze'

	user_profile = models.OneToOneField(UserProfile, related_name='experience_section')
	is_active = models.BooleanField(default=True)

class EducationSection(models.Model):
	class Meta:
		app_label = 'mycraze'

	user_profile = models.OneToOneField(UserProfile, related_name='education_section')
	is_active = models.BooleanField(default=True)

class PublicationSection(models.Model):
	class Meta:
		app_label = 'mycraze'

	user_profile = models.OneToOneField(UserProfile, related_name='publication_section')
	is_active = models.BooleanField(default=True)

class CertificationSection(models.Model):
	class Meta:
		app_label = 'mycraze'

	user_profile = models.OneToOneField(UserProfile, related_name='certification_section')
	is_active = models.BooleanField(default=True)

class SkillSection(models.Model):
	class Meta:
		app_label = 'mycraze'

	user_profile = models.OneToOneField(UserProfile, related_name='skill_section')
	is_active = models.BooleanField(default=True)

class CourseSection(models.Model):
	class Meta:
		app_label = 'mycraze'

	user_profile = models.OneToOneField(UserProfile, related_name='course_section')
	is_active = models.BooleanField(default=True)

class AwardSection(models.Model):
	class Meta:
		app_label = 'mycraze'

	user_profile = models.OneToOneField(UserProfile, related_name='award_section')
	is_active = models.BooleanField(default=True)

class LanguageSection(models.Model):
	class Meta:
		app_label = 'mycraze'

	user_profile = models.OneToOneField(UserProfile, related_name='language_section')
	is_active = models.BooleanField(default=True)

class ContactSection(models.Model):
	class Meta:
		app_label = 'mycraze'

	user_profile = models.OneToOneField(UserProfile, related_name='contact_section')
	personal_email = models.CharField(max_length=40)
	phone_number = models.CharField(max_length=20)
	is_active = models.BooleanField(default=True)