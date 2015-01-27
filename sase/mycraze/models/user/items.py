from django.db import models
from mycraze.models.user.sections import ExperienceSection
from mycraze.models.user.sections import ProjectSection

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