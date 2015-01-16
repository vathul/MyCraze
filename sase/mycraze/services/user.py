from mycraze.models.user.profile import UserProfile
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
		user_profile = current_user.userProfile
		user_profile.description = updated_profile.description
		user_profile.save()
		return current_user