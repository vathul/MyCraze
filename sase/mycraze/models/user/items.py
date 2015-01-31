from django.db import models
from mycraze.models.user.sections import AwardSection
from mycraze.models.user.sections import CertificationSection
from mycraze.models.user.sections import CourseSection
from mycraze.models.user.sections import EducationSection
from mycraze.models.user.sections import ExperienceSection
from mycraze.models.user.sections import ProjectSection
from mycraze.models.user.sections import PublicationSection
from mycraze.models.user.sections import SkillSection

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

class CertificationItem(models.Model):
	class Meta:
		app_label = 'mycraze'

	title = models.CharField(max_length=200)
	certifier = models.CharField(max_length=100)
	certification_section = models.ForeignKey(CertificationSection, related_name="certification_items")

class AwardItem(models.Model):
	class Meta:
		app_label = 'mycraze'

	title = models.CharField(max_length=200)
	issuer = models.CharField(max_length=100)
	description = models.CharField(max_length=400)
	award_section = models.ForeignKey(AwardSection, related_name="award_items")

class SkillItem(models.Model):
	class Meta:
		app_label = 'mycraze'

	skill = models.CharField(max_length=100)
	skill_section = models.ForeignKey(SkillSection, related_name="skill_items")

class CourseItem(models.Model):
	class Meta:
		app_label = 'mycraze'

	title = models.CharField(max_length=100)
	code = models.CharField(max_length=20)
	course_section = models.ForeignKey(CourseSection, related_name="course_items")	