from mycraze.models.user.sections import SummarySection
from mycraze.models.user.sections import ExperienceSection
from mycraze.models.user.sections import ContactSection

class UserProfileService:
	def create_sections(user):
		#create sections here
		summary_section = SummarySection(user_profile = user.user_profile)
		experience_section = ExperienceSection(user_profile = user.user_profile)
		contact_section = ContactSection(user_profile = user.user_profile)

		#add the sections here
		summary_section.user_profile = user.user_profile
		experience_section.user_profile = user.user_profile
		contact_section.user_profile = user.user_profile

		#save the sections here
		summary_section.save()
		experience_section.save()
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

	def edit_contact_content(current_user, contact_content):
		user_profile = current_user.user_profile
		contact_section,created = ContactSection.objects.get_or_create(user_profile = user_profile)
		contact_section.personal_email = contact_content.personal_email
		contact_section.phone_number = contact_content.phone_number
		contact_section.save()
		return contact_section