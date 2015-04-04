"""This module contains model classes pertaining to various items in the user
resume page"""

__author__ = "Srikrishnan Suresh"
__copyright__ = "Copyright 2015, MyCraze"
__version__ = "1.0.1"

from django.db import models

from mycraze.models.user.sections import AwardSection
from mycraze.models.user.sections import CertificationSection
from mycraze.models.user.sections import CourseSection
from mycraze.models.user.sections import EducationSection
from mycraze.models.user.sections import ExperienceSection
from mycraze.models.user.sections import LanguageSection
from mycraze.models.user.sections import ProjectSection
from mycraze.models.user.sections import PublicationSection
from mycraze.models.user.sections import SkillSection


class ExperienceItem(models.Model):
    """This module is the model class that represents an experience item within
    an experience section in user resume.
    Refer py:module:: mycraze.models.user.sections.ExperienceSection
    Can be accessed by experience_section.experience_items.
    """

    class Meta:
        app_label = 'mycraze'

    role = models.CharField(max_length=40)
    organization = models.CharField(max_length=60)
    description = models.CharField(max_length=400)
    experience_section = models.ForeignKey(ExperienceSection, related_name="experience_items")

class ProjectItem(models.Model):
    """This module is the model class that represents a project item within
    a project section in user resume.
    Refer py:module:: mycraze.models.user.sections.ProjectSection
    Can be accessed by project_section.project_items.
    """

    class Meta:
        app_label = 'mycraze'

    title = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    project_section = models.ForeignKey(ProjectSection, related_name="project_items")

class EducationItem(models.Model):
    """This module is the model class that represents an education item within
    an education section in user resume.
    Refer py:module:: mycraze.models.user.sections.EducationSection
    Can be accessed by education_section.education_items.
    """

    class Meta:
        app_label = 'mycraze'

    school = models.CharField(max_length=200)
    degree = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    education_section = models.ForeignKey(EducationSection, related_name="education_items")

class PublicationItem(models.Model):
    """This module is the model class that represents a publication item within
    a publication section in user resume.
    Refer py:module:: mycraze.models.user.sections.PublicationSection
    Can be accessed by publication_section.publication_items.
    """

    class Meta:
        app_label = 'mycraze'

    title = models.CharField(max_length=200)
    publisher = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    publication_section = models.ForeignKey(PublicationSection, related_name="publication_items")

class CertificationItem(models.Model):
    """This module is the model class that represents a certification item within
    a certification section in user resume.
    Refer py:module:: mycraze.models.user.sections.CertificationSection
    Can be accessed by certification_section.certification_items.
    """

    class Meta:
        app_label = 'mycraze'

    title = models.CharField(max_length=200)
    certifier = models.CharField(max_length=100)
    certification_section = models.ForeignKey(CertificationSection, related_name="certification_items")

class AwardItem(models.Model):
    """This module is the model class that represents an award item within
    an award section in user resume.
    Refer py:module:: mycraze.models.user.sections.AwardSection
    Can be accessed by award_section.award_items.
    """

    class Meta:
        app_label = 'mycraze'

    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    award_section = models.ForeignKey(AwardSection, related_name="award_items")

class SkillItem(models.Model):
    """This module is the model class that represents a skill item within
    a skill section in user resume.
    Refer py:module:: mycraze.models.user.sections.SkillSection
    Can be accessed by skill_section.skill_items.
    """

    class Meta:
        app_label = 'mycraze'

    skill = models.CharField(max_length=100)
    skill_section = models.ForeignKey(SkillSection, related_name="skill_items")

class CourseItem(models.Model):
    """This module is the model class that represents a course item within
    a course section in user resume.
    Refer py:module:: mycraze.models.user.sections.CourseSection
    Can be accessed by course_section.course_items.
    """

    class Meta:
        app_label = 'mycraze'

    title = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    course_section = models.ForeignKey(CourseSection, related_name="course_items")

class LanguageItem(models.Model):
    """This module is the model class that represents a language item within
    a language section in user resume.
    Refer py:module:: mycraze.models.user.sections.LanguageSection
    Can be accessed by language_section.language_items.
    """

    class Meta:
        app_label = 'mycraze'

    language = models.CharField(max_length=100)
    language_section = models.ForeignKey(LanguageSection, related_name="language_items")