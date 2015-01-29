from django.db import models
from mycraze.models.user.sections import EducationSection
from mycraze.models.user.sections import ExperienceSection
from mycraze.models.user.sections import ProjectSection
from mycraze.models.user.sections import PublicationSection

class ExperienceItem(models.Model):
	class Meta:
		app_label = 'mycraze'

	role = models.CharField(max_length=40)
	organization = models.CharField(max_length=60)
	description = models.CharField(max_length=400)
	experience_section = models.ForeignKey(ExperienceSection, related_name="experience_items")

class ProjectItem(models.Model):
	class Meta:
		app_label = 'mycraze'

	title = models.CharField(max_length=100)
	url = models.CharField(max_length=200)
	description = models.CharField(max_length=400)
	project_section = models.ForeignKey(ProjectSection, related_name="project_items")

class EducationItem(models.Model):
	class Meta:
		app_label = 'mycraze'

	school = models.CharField(max_length=200)
	degree = models.CharField(max_length=100)
	description = models.CharField(max_length=400)
	education_section = models.ForeignKey(EducationSection, related_name="education_items")

class PublicationItem(models.Model):
	class Meta:
		app_label = 'mycraze'

	title = models.CharField(max_length=200)
	publisher = models.CharField(max_length=100)
	description = models.CharField(max_length=400)
	publication_section = models.ForeignKey(PublicationSection, related_name="publication_items")