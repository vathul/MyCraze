from mycraze.models.user.sections import SummarySection
from mycraze.models.user.sections import EducationSection
from mycraze.models.user.items import EducationItem
from mycraze.models.user.sections import ExperienceSection
from mycraze.models.user.items import ExperienceItem
from mycraze.models.user.sections import ProjectSection
from mycraze.models.user.items import ProjectItem
from mycraze.models.user.sections import ContactSection

class UserProfileService:
	def create_sections(user):
		#create sections here
		summary_section = SummarySection(user_profile = user.user_profile)
		experience_section = ExperienceSection(user_profile = user.user_profile)
		project_section = ProjectSection(user_profile = user.user_profile)
		education_section = EducationSection(user_profile = user.user_profile)
		contact_section = ContactSection(user_profile = user.user_profile)

		#add the sections here
		summary_section.user_profile = user.user_profile
		experience_section.user_profile = user.user_profile
		project_section.user_profile = user.user_profile
		education_section.user_profile = user.user_profile
		contact_section.user_profile = user.user_profile

		#save the sections here
		summary_section.save()
		experience_section.save()
		project_section.save()
		education_section.save()
		contact_section.save()

	def save_user_profile(current_user, updated_user, updated_profile):
		current_user.first_name = updated_user.first_name
		current_user.last_name = updated_user.last_name
		current_user.save()
		updated_profile.user = current_user
		updated_profile.save()
		UserProfileService.create_sections(current_user)
		return current_user

	def edit_user_profile(current_user, updated_user, updated_profile):
		current_user.first_name = updated_user.first_name
		current_user.last_name = updated_user.last_name
		current_user.save()
		user_profile = current_user.user_profile
		user_profile.description = updated_profile.description
		user_profile.save()
		return current_user

	def edit_summary_content(current_user, summary_content):
		user_profile = current_user.user_profile
		summary_section,created = SummarySection.objects.get_or_create(user_profile = user_profile)
		summary_section.content = summary_content
		summary_section.save()
		return summary_section

	def	edit_experience_item(current_user, item_content):
		experience_section = current_user.user_profile.experience_section
		if item_content.id == "0":
			experience_item = ExperienceItem(experience_section=experience_section, role=item_content.role,organization=item_content.organization,description=item_content.description)
		else:
			experience_item = ExperienceItem(id=item_content.id, experience_section=experience_section, role=item_content.role,organization=item_content.organization,description=item_content.description)			
		experience_item.save()
		return experience_item

	def	edit_project_item(current_user, item_content):
		project_section = current_user.user_profile.project_section
		if item_content.id == "0":
			project_item = ProjectItem(project_section=project_section, title=item_content.title,url=item_content.url,description=item_content.description)
		else:
			project_item = ProjectItem(id=item_content.id, project_section=project_section, title=item_content.title,url=item_content.url,description=item_content.description)
		project_item.save()
		return project_item

	def	edit_education_item(current_user, item_content):
		education_section = current_user.user_profile.education_section
		if item_content.id == "0":
			education_item = EducationItem(education_section=education_section, school=item_content.school,degree=item_content.degree,description=item_content.description)
		else:
			education_item = EducationItem(id=item_content.id, education_section=education_section, school=item_content.school,degree=item_content.degree,description=item_content.description)
		education_item.save()
		return education_item

	def edit_contact_content(current_user, contact_content):
		user_profile = current_user.user_profile
		contact_section,created = ContactSection.objects.get_or_create(user_profile = user_profile)
		contact_section.personal_email = contact_content.personal_email
		contact_section.phone_number = contact_content.phone_number
		contact_section.save()
		return contact_section