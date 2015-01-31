from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from mycraze.models.form.items import AwardItemForm
from mycraze.models.form.items import CertificationItemForm
from mycraze.models.form.items import CourseItemForm
from mycraze.models.form.items import EducationItemForm
from mycraze.models.form.items import ExperienceItemForm
from mycraze.models.form.items import ProjectItemForm
from mycraze.models.form.items import PublicationItemForm
from mycraze.models.form.items import SkillItemForm
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
@csrf_exempt
def edit_education(request):
	item_form = EducationItemForm(request.POST)
	item_id = request.POST['item_id']
	if item_form.is_valid():
		item = item_form.save(commit=False)
		item.id = item_id
		education_item = UserProfileService.edit_education_item(request.user, item)
	html = render_to_string('mycraze/item/education.html', 
		{'item': education_item})
	return HttpResponse(html)

@login_required
@csrf_exempt
def edit_publication(request):
	item_form = PublicationItemForm(request.POST)
	item_id = request.POST['item_id']
	if item_form.is_valid():
		item = item_form.save(commit=False)
		item.id = item_id
		publication_item = UserProfileService.edit_publication_item(request.user, item)
	html = render_to_string('mycraze/item/publication.html', 
		{'item': publication_item})
	return HttpResponse(html)

@login_required
@csrf_exempt
def edit_certification(request):
	item_form = CertificationItemForm(request.POST)
	item_id = request.POST['item_id']
	if item_form.is_valid():
		item = item_form.save(commit=False)
		item.id = item_id
		certification_item = UserProfileService.edit_certification_item(request.user, item)
	html = render_to_string('mycraze/item/certification.html', 
		{'item': certification_item})
	return HttpResponse(html)

@login_required
@csrf_exempt
def edit_skill(request):
	item_form = SkillItemForm(request.POST)
	item_id = request.POST['item_id']
	if item_form.is_valid():
		item = item_form.save(commit=False)
		item.id = item_id
		skill_item = UserProfileService.edit_skill_item(request.user, item)
	html = render_to_string('mycraze/item/skill.html', 
		{'item': skill_item})
	return HttpResponse(html)

@login_required
@csrf_exempt
def edit_course(request):
	item_form = CourseItemForm(request.POST)
	item_id = request.POST['item_id']
	if item_form.is_valid():
		item = item_form.save(commit=False)
		item.id = item_id
		course_item = UserProfileService.edit_course_item(request.user, item)
	html = render_to_string('mycraze/item/course.html', 
		{'item': course_item})
	return HttpResponse(html)

@login_required
@csrf_exempt
def edit_award(request):
	item_form = AwardItemForm(request.POST)
	item_id = request.POST['item_id']
	if item_form.is_valid():
		item = item_form.save(commit=False)
		item.id = item_id
		award_item = UserProfileService.edit_award_item(request.user, item)
	html = render_to_string('mycraze/item/award.html', 
		{'item': award_item})
	return HttpResponse(html)

@login_required
def edit_contact(request):
	section_form = ContactSectionForm(request.POST)
	if section_form.is_valid():
		section = section_form.save(commit=False)
		contact_section = UserProfileService.edit_contact_content(request.user, section)
	return JsonResponse({'personal_email': contact_section.personal_email, "phone_number": contact_section.phone_number})