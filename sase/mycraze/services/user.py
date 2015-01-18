from mycraze.models.user.sections import SummarySection

class UserProfileService:
	def save_user_profile(current_user, updated_user, updated_profile):
		current_user.first_name = updated_user.first_name
		current_user.last_name = updated_user.last_name
		current_user.save()
		updated_profile.user = current_user
		updated_profile.save()
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