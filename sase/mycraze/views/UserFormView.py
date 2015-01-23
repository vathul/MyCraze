from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import render_to_string
from mycraze.models.form.items import ExperienceItemForm
from mycraze.models.user.items import ExperienceItem
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