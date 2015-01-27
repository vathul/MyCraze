from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from mycraze.models.form.items import ExperienceItemForm
from mycraze.models.form.items import ProjectItemForm
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
def edit_experience(request):
	item_form = ExperienceItemForm(request.POST)
	item_id = request.POST['item_id']
	if item_form.is_valid():
		item = item_form.save(commit=False)
		item.id = item_id
		experience_item = UserProfileService.edit_experience_item(request.user, item)
	html = render_to_string('mycraze/item/experience.html', 
		{'item': experience_item})
	return HttpResponse(html)

@login_required
@csrf_exempt
def edit_project(request):
	item_form = ProjectItemForm(request.POST)
	item_id = request.POST['item_id']
	if item_form.is_valid():
		item = item_form.save(commit=False)
		item.id = item_id
		project_item = UserProfileService.edit_project_item(request.user, item)
	html = render_to_string('mycraze/item/project.html', 
		{'item': project_item})
	return HttpResponse(html)

@login_required
def edit_contact(request):
	section_form = ContactSectionForm(request.POST)
	if section_form.is_valid():
		section = section_form.save(commit=False)
		contact_section = UserProfileService.edit_contact_content(request.user, section)
	return JsonResponse({'personal_email': contact_section.personal_email, "phone_number": contact_section.phone_number})
