from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import render_to_string
from mycraze.models.form.items import EducationItemForm
from mycraze.models.user.items import EducationItem
from mycraze.models.form.items import ExperienceItemForm
from mycraze.models.user.items import ExperienceItem
from mycraze.models.form.items import ProjectItemForm
from mycraze.models.user.items import ProjectItem
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