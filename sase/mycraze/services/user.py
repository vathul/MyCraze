class UserProfileService:
	def save_user_profile(current_user, updated_user, updated_profile):
		try:
			current_user.first_name = updated_user.first_name
			current_user.last_name = updated_user.last_name
			current_user.save()
			updated_profile.user = current_user
			updated_profile.save()
		except IntegrityError:
			print("Something wrong.")
