from mycraze.models.user.items import AwardItem
from mycraze.models.user.items import CertificationItem
from mycraze.models.user.items import CourseItem
from mycraze.models.user.items import EducationItem
from mycraze.models.user.items import ExperienceItem
from mycraze.models.user.items import LanguageItem
from mycraze.models.user.items import ProjectItem
from mycraze.models.user.items import PublicationItem
from mycraze.models.user.items import SkillItem
from mycraze.models.user.profile import UserProfile
from mycraze.models.user.sections import AwardSection
from mycraze.models.user.sections import CertificationSection
from mycraze.models.user.sections import ContactSection
from mycraze.models.user.sections import CourseSection
from mycraze.models.user.sections import EducationSection
from mycraze.models.user.sections import ExperienceSection
from mycraze.models.user.sections import LanguageSection
from mycraze.models.user.sections import ProfileSection
from mycraze.models.user.sections import ProjectSection
from mycraze.models.user.sections import PublicationSection
from mycraze.models.user.sections import SkillSection
from mycraze.models.user.sections import SummarySection


class UserProfileService:
	@staticmethod
	def create_sections(user):
		#create sections here
		summary_section = SummarySection(user_profile = user.user_profile)
		experience_section = ExperienceSection(user_profile = user.user_profile)
		project_section = ProjectSection(user_profile = user.user_profile)
		education_section = EducationSection(user_profile = user.user_profile)
		profile_section = ProfileSection(user_profile = user.user_profile)
		publication_section = PublicationSection(user_profile = user.user_profile)
		certification_section = CertificationSection(user_profile = user.user_profile)
		skill_section = SkillSection(user_profile = user.user_profile)
		course_section = CourseSection(user_profile = user.user_profile)
		award_section = AwardSection(user_profile = user.user_profile)
		language_section = LanguageSection(user_profile = user.user_profile)
		contact_section = ContactSection(user_profile = user.user_profile)

		#add the sections here
		summary_section.user_profile = user.user_profile
		experience_section.user_profile = user.user_profile
		project_section.user_profile = user.user_profile
		education_section.user_profile = user.user_profile
		profile_section.user_profile = user.user_profile
		publication_section.user_profile = user.user_profile
		certification_section.user_profile = user.user_profile
		skill_section.user_profile = user.user_profile
		course_section.user_profile = user.user_profile
		award_section.user_profile = user.user_profile
		language_section.user_profile = user.user_profile
		contact_section.user_profile = user.user_profile

		#save the sections here
		summary_section.save()
		experience_section.save()
		project_section.save()
		education_section.save()
		profile_section.save()
		publication_section.save()
		certification_section.save()
		skill_section.save()
		course_section.save()
		award_section.save()
		language_section.save()
		contact_section.save()

	@staticmethod
	def has_user_profile(user):
		return True if UserProfile.objects.select_related('user').filter(user=user) else False
		
	@staticmethod
	def save_user_profile(current_user, updated_user, updated_profile):
		current_user.first_name = updated_user.first_name
		current_user.last_name = updated_user.last_name
		current_user.save()
		updated_profile.user = current_user
		updated_profile.save()
		UserProfileService.create_sections(current_user)
		return current_user

	@staticmethod
	def edit_user_profile(current_user, updated_user, updated_profile):
		current_user.first_name = updated_user.first_name
		current_user.last_name = updated_user.last_name
		current_user.save()
		user_profile = current_user.user_profile
		user_profile.description = updated_profile.description
		user_profile.save()
		return current_user

	@staticmethod
	def edit_summary_content(current_user, summary_content):
		user_profile = current_user.user_profile
		summary_section,created = SummarySection.objects.get_or_create(user_profile = user_profile)
		summary_section.content = summary_content
		summary_section.save()
		return summary_section

	@staticmethod
	def edit_summary_status(current_user, status):
		user_profile = current_user.user_profile
		summary_section = user_profile.summary_section
		summary_section.is_active = status
		summary_section.save()
		return summary_section.is_active

	@staticmethod
	def	edit_experience_item(current_user, item_content):
		experience_section = current_user.user_profile.experience_section
		if item_content.id == "0":
			experience_item = ExperienceItem(experience_section=experience_section, role=item_content.role,organization=item_content.organization,description=item_content.description)
		else:
			experience_item = ExperienceItem(id=item_content.id, experience_section=experience_section, role=item_content.role,organization=item_content.organization,description=item_content.description)			
		experience_item.save()
		return experience_item

	@staticmethod
	def edit_experience_status(current_user, status):
		user_profile = current_user.user_profile
		experience_section = user_profile.experience_section
		experience_section.is_active = status
		experience_section.save()
		return experience_section.is_active

	@staticmethod
	def	edit_project_item(current_user, item_content):
		project_section = current_user.user_profile.project_section
		if item_content.id == "0":
			project_item = ProjectItem(project_section=project_section, title=item_content.title,url=item_content.url,description=item_content.description)
		else:
			project_item = ProjectItem(id=item_content.id, project_section=project_section, title=item_content.title,url=item_content.url,description=item_content.description)
		project_item.save()
		return project_item

	@staticmethod
	def edit_project_status(current_user, status):
		user_profile = current_user.user_profile
		project_section = user_profile.project_section
		project_section.is_active = status
		project_section.save()
		return project_section.is_active

	@staticmethod
	def	edit_education_item(current_user, item_content):
		education_section = current_user.user_profile.education_section
		if item_content.id == "0":
			education_item = EducationItem(education_section=education_section, school=item_content.school,degree=item_content.degree,description=item_content.description)
		else:
			education_item = EducationItem(id=item_content.id, education_section=education_section, school=item_content.school,degree=item_content.degree,description=item_content.description)
		education_item.save()
		return education_item

	@staticmethod
	def edit_education_status(current_user, status):
		user_profile = current_user.user_profile
		education_section = user_profile.education_section
		education_section.is_active = status
		education_section.save()
		return education_section.is_active

	@staticmethod
	def edit_profile_status(current_user, status):
		user_profile = current_user.user_profile
		profile_section = user_profile.profile_section
		profile_section.is_active = status
		profile_section.save()
		return profile_section.is_active

	@staticmethod
	def	edit_publication_item(current_user, item_content):
		publication_section = current_user.user_profile.publication_section
		if item_content.id == "0":
			publication_item = PublicationItem(publication_section=publication_section, title=item_content.title,publisher=item_content.publisher,description=item_content.description)
		else:
			publication_item = PublicationItem(id=item_content.id, publication_section=publication_section, title=item_content.title,publisher=item_content.publisher,description=item_content.description)
		publication_item.save()
		return publication_item

	@staticmethod
	def edit_publication_status(current_user, status):
		user_profile = current_user.user_profile
		publication_section = user_profile.publication_section
		publication_section.is_active = status
		publication_section.save()
		return publication_section.is_active

	@staticmethod
	def	edit_certification_item(current_user, item_content):
		certification_section = current_user.user_profile.certification_section
		if item_content.id == "0":
			certification_item = CertificationItem(certification_section=certification_section, title=item_content.title,certifier=item_content.certifier)
		else:
			certification_item = CertificationItem(id=item_content.id, certification_section=certification_section, title=item_content.title,certifier=item_content.certifier)
		certification_item.save()
		return certification_item

	@staticmethod
	def edit_certification_status(current_user, status):
		user_profile = current_user.user_profile
		certification_section = user_profile.certification_section
		certification_section.is_active = status
		certification_section.save()
		return certification_section.is_active

	@staticmethod
	def	edit_skill_item(current_user, item_content):
		skill_section = current_user.user_profile.skill_section
		if item_content.id == "0":
			skill_item = SkillItem(skill_section=skill_section, skill=item_content.skill)
		else:
			skill_item = SkillItem(id=item_content.id, skill_section=skill_section, skill=item_content.skill)
		skill_item.save()
		return skill_item

	@staticmethod
	def edit_skill_status(current_user, status):
		user_profile = current_user.user_profile
		skill_section = user_profile.skill_section
		skill_section.is_active = status
		skill_section.save()
		return skill_section.is_active

	@staticmethod
	def	edit_course_item(current_user, item_content):
		course_section = current_user.user_profile.course_section
		if item_content.id == "0":
			course_item = CourseItem(course_section=course_section, title=item_content.title, code=item_content.code)
		else:
			course_item = CourseItem(id=item_content.id, course_section=course_section, title=item_content.title, code=item_content.code)
		course_item.save()
		return course_item

	@staticmethod
	def edit_course_status(current_user, status):
		user_profile = current_user.user_profile
		course_section = user_profile.course_section
		course_section.is_active = status
		course_section.save()
		return course_section.is_active

	@staticmethod
	def	edit_award_item(current_user, item_content):
		award_section = current_user.user_profile.award_section
		if item_content.id == "0":
			award_item = AwardItem(award_section=award_section, title=item_content.title,issuer=item_content.issuer, description=item_content.description)
		else:
			award_item = AwardItem(id=item_content.id, award_section=award_section, title=item_content.title,issuer=item_content.issuer, description=item_content.description)
		award_item.save()
		return award_item

	@staticmethod
	def edit_award_status(current_user, status):
		user_profile = current_user.user_profile
		award_section = user_profile.award_section
		award_section.is_active = status
		award_section.save()
		return award_section.is_active

	@staticmethod
	def	edit_language_item(current_user, item_content):
		language_section = current_user.user_profile.language_section
		if item_content.id == "0":
			language_item = LanguageItem(language_section=language_section, language=item_content.language)
		else:
			language_item = LanguageItem(id=item_content.id, language_section=language_section, language=item_content.language)
		language_item.save()
		return language_item

	@staticmethod
	def edit_language_status(current_user, status):
		user_profile = current_user.user_profile
		language_section = user_profile.language_section
		language_section.is_active = status
		language_section.save()
		return language_section.is_active

	@staticmethod	
	def edit_contact_content(current_user, contact_content):
		user_profile = current_user.user_profile
		contact_section,created = ContactSection.objects.get_or_create(user_profile = user_profile)
		contact_section.personal_email = contact_content.personal_email
		contact_section.phone_number = contact_content.phone_number
		contact_section.save()
		return contact_section

	@staticmethod	
	def edit_contact_status(current_user, status):
		user_profile = current_user.user_profile
		contact_section = user_profile.contact_section
		contact_section.is_active = status
		contact_section.save()
		return contact_section.is_active