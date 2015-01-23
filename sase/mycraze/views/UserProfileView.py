from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from mycraze.models.form.items import ExperienceItemForm
from mycraze.models.form.sections import ContactSectionForm
from mycraze.services.user import UserProfileService
from mycraze.utils.http import JsonResponse

@login_required
def edit_summary(request):
	summary_content = request.POST['content']
	summary_section = UserProfileService.edit_summary_content(request.user, summary_content)
	return JsonResponse({'content': summary_section.content})

@login_required
@csrf_exempt
def add_experience(request):
	item_form = ExperienceItemForm(request.POST)
	if item_form.is_valid():
		item = item_form.save(commit=False)
		experience_item = UserProfileService.add_experience_item(request.user, item)
	return JsonResponse({'role': item.role, 'organization': item.organization, 'description': item.description})

@login_required
def edit_contact(request):
	section_form = ContactSectionForm(request.POST)
	if section_form.is_valid():
		section = section_form.save(commit=False)
		contact_section = UserProfileService.edit_contact_content(request.user, section)
	return JsonResponse({'personal_email': contact_section.personal_email, "phone_number": contact_section.phone_number})
