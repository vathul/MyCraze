from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import render_to_string
from mycraze.models.form.items import AwardItemForm
from mycraze.models.user.items import AwardItem
from mycraze.models.form.items import CertificationItemForm
from mycraze.models.user.items import CertificationItem
from mycraze.models.form.items import CourseItemForm
from mycraze.models.user.items import CourseItem
from mycraze.models.form.items import EducationItemForm
from mycraze.models.user.items import EducationItem
from mycraze.models.form.items import ExperienceItemForm
from mycraze.models.user.items import ExperienceItem
from mycraze.models.form.items import LanguageItemForm
from mycraze.models.user.items import LanguageItem
from mycraze.models.form.items import ProjectItemForm
from mycraze.models.user.items import ProjectItem
from mycraze.models.form.items import PublicationItemForm
from mycraze.models.user.items import PublicationItem
from mycraze.models.form.items import SkillItemForm
from mycraze.models.user.items import SkillItem

@login_required
def get_experience_form(request):
	item_id = request.POST['id']
	if item_id == "0":
		experience_form = ExperienceItemForm()
	else:
		experience_item = ExperienceItem.objects.get(id=item_id)
		experience_form = ExperienceItemForm(instance=experience_item)
	html = render_to_string('mycraze/form/edit-experience-form.html', 
		{'experience_form': experience_form})
	return HttpResponse(html)

@login_required
def get_project_form(request):
	item_id = request.POST['id']
	if item_id == "0":
		project_form = ProjectItemForm()
	else:
		project_item = ProjectItem.objects.get(id=item_id)
		project_form = ProjectItemForm(instance=project_item)
	html = render_to_string('mycraze/form/edit-project-form.html', 
		{'project_form': project_form})
	return HttpResponse(html)

@login_required
def get_publication_form(request):
	item_id = request.POST['id']
	if item_id == "0":
		publication_form = PublicationItemForm()
	else:
		publication_item = PublicationItem.objects.get(id=item_id)
		publication_form = PublicationItemForm(instance=publication_item)
	html = render_to_string('mycraze/form/edit-publication-form.html', 
		{'publication_form': publication_form})
	return HttpResponse(html)

@login_required
def get_education_form(request):
	item_id = request.POST['id']
	if item_id == "0":
		education_form = EducationItemForm()
	else:
		education_item = EducationItem.objects.get(id=item_id)
		education_form = EducationItemForm(instance=education_item)
	html = render_to_string('mycraze/form/edit-education-form.html', 
		{'education_form': education_form})
	return HttpResponse(html)

@login_required
def get_certification_form(request):
	item_id = request.POST['id']
	if item_id == "0":
		certification_form = CertificationItemForm()
	else:
		certification_item = CertificationItem.objects.get(id=item_id)
		certification_form = CertificationItemForm(instance=certification_item)
	html = render_to_string('mycraze/form/edit-certification-form.html', 
		{'certification_form': certification_form})
	return HttpResponse(html)

@login_required
def get_course_form(request):
	item_id = request.POST['id']
	if item_id == "0":
		course_form = CourseItemForm()
	else:
		course_item = CourseItem.objects.get(id=item_id)
		course_form = CourseItemForm(instance=course_item)
	html = render_to_string('mycraze/form/edit-course-form.html', 
		{'course_form': course_form})
	return HttpResponse(html)

@login_required
def get_skill_form(request):
	item_id = request.POST['id']
	if item_id == "0":
		skill_form = SkillItemForm()
	else:
		skill_item = SkillItem.objects.get(id=item_id)
		skill_form = SkillItemForm(instance=skill_item)
	html = render_to_string('mycraze/form/edit-skill-form.html', 
		{'skill_form': skill_form})
	return HttpResponse(html)

@login_required
def get_award_form(request):
	item_id = request.POST['id']
	if item_id == "0":
		award_form = AwardItemForm()
	else:
		award_item = AwardItem.objects.get(id=item_id)
		award_form = AwardItemForm(instance=award_item)
	html = render_to_string('mycraze/form/edit-award-form.html', 
		{'award_form': award_form})
	return HttpResponse(html)

@login_required
def get_language_form(request):
	item_id = request.POST['id']
	if item_id == "0":
		language_form = LanguageItemForm()
	else:
		language_item = LanguageItem.objects.get(id=item_id)
		language_form = LanguageItemForm(instance=language_item)
	html = render_to_string('mycraze/form/edit-language-form.html', 
		{'language_form': language_form})
	return HttpResponse(html)