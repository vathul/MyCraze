"""This module contains view classes pertaining to various forms for editing
the items under sections in resume page."""

__author__ = "Srikrishnan Suresh"
__copyright__ = "Copyright 2015, MyCraze"
__version__ = "1.0.1"

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt

from mycraze.models.form.items import AwardItemForm
from mycraze.models.form.items import CertificationItemForm
from mycraze.models.form.items import CourseItemForm
from mycraze.models.form.items import EducationItemForm
from mycraze.models.form.items import ExperienceItemForm
from mycraze.models.form.items import LanguageItemForm
from mycraze.models.form.items import ProjectItemForm
from mycraze.models.form.items import PublicationItemForm
from mycraze.models.form.items import SkillItemForm
from mycraze.models.form.sections import ContactSectionForm
from mycraze.services.user import UserProfileService
from mycraze.utils.http import JsonResponse


@login_required
def edit_summary(request):
    """This function handles user request to edit the summary content. It
    returns the edited content in json format. 
    """

    summary_content = request.POST['content']
    summary_section = UserProfileService.edit_summary_content(request.user, summary_content)
    return JsonResponse({'content': summary_section.content})

@login_required
def edit_summary_status(request):
    """This function handles user request to edit the active status of
    summary section. It returns the new active status of the section. 
    """

    status = True if request.POST['status'] == 'true' else False
    status = UserProfileService.edit_summary_status(request.user, status)
    return JsonResponse({'status': status})

@login_required
@csrf_exempt
def edit_experience(request):
    """This function handles user request to edit the experience content. It
    returns the edited content in json format. 
    """

    item_form = ExperienceItemForm(request.POST)
    item_id = request.POST['item_id']
    if item_form.is_valid():
        item = item_form.save(commit=False)
        item.id = item_id
        experience_item = UserProfileService.edit_experience_item(request.user, item)
    html = render_to_string('mycraze/item/experience.html', 
        {'item': experience_item, 'has_edit_permission': True})
    return HttpResponse(html)

@login_required
def edit_experience_status(request):
    """This function handles user request to edit the active status of
    experience section. It returns the new active status of the section. 
    """
    
    status = True if request.POST['status'] == 'true' else False
    status = UserProfileService.edit_experience_status(request.user, status)
    return JsonResponse({'status': status})

@login_required
@csrf_exempt
def edit_project(request):
    """This function handles user request to edit the project content. It
    returns the edited content in json format. 
    """

    item_form = ProjectItemForm(request.POST)
    item_id = request.POST['item_id']
    if item_form.is_valid():
        item = item_form.save(commit=False)
        item.id = item_id
        project_item = UserProfileService.edit_project_item(request.user, item)
    html = render_to_string('mycraze/item/project.html', 
        {'item': project_item, 'has_edit_permission': True})
    return HttpResponse(html)

def edit_project_status(request):
    """This function handles user request to edit the active status of
    project section. It returns the new active status of the section. 
    """

    status = True if request.POST['status'] == 'true' else False
    status = UserProfileService.edit_project_status(request.user, status)
    return JsonResponse({'status': status})

@login_required
@csrf_exempt
def edit_education(request):
    """This function handles user request to edit the education content. It
    returns the edited content in json format. 
    """

    item_form = EducationItemForm(request.POST)
    item_id = request.POST['item_id']
    if item_form.is_valid():
        item = item_form.save(commit=False)
        item.id = item_id
        education_item = UserProfileService.edit_education_item(request.user, item)
    html = render_to_string('mycraze/item/education.html', 
        {'item': education_item, 'has_edit_permission': True})
    return HttpResponse(html)

def edit_education_status(request):
    """This function handles user request to edit the active status of
    education section. It returns the new active status of the section. 
    """

    status = True if request.POST['status'] == 'true' else False
    status = UserProfileService.edit_education_status(request.user, status)
    return JsonResponse({'status': status})

def edit_profile_status(request):
    

    status = True if request.POST['status'] == 'true' else False
    status = UserProfileService.edit_profile_status(request.user, status)
    return JsonResponse({'status': status})

@login_required
@csrf_exempt
def edit_publication(request):
    """This function handles user request to edit the publication content. It
    returns the edited content in json format. 
    """

    item_form = PublicationItemForm(request.POST)
    item_id = request.POST['item_id']
    if item_form.is_valid():
        item = item_form.save(commit=False)
        item.id = item_id
        publication_item = UserProfileService.edit_publication_item(request.user, item)
    html = render_to_string('mycraze/item/publication.html', 
        {'item': publication_item, 'has_edit_permission': True})
    return HttpResponse(html)

def edit_publication_status(request):
    """This function handles user request to edit the active status of
    publication section. It returns the new active status of the section. 
    """

    status = True if request.POST['status'] == 'true' else False
    status = UserProfileService.edit_publication_status(request.user, status)
    return JsonResponse({'status': status})

@login_required
@csrf_exempt
def edit_certification(request):
    """This function handles user request to edit the certification content. It
    returns the edited content in json format. 
    """

    item_form = CertificationItemForm(request.POST)
    item_id = request.POST['item_id']
    if item_form.is_valid():
        item = item_form.save(commit=False)
        item.id = item_id
        certification_item = UserProfileService.edit_certification_item(request.user, item)
    html = render_to_string('mycraze/item/certification.html', 
        {'item': certification_item, 'has_edit_permission': True})
    return HttpResponse(html)

def edit_certification_status(request):
    """This function handles user request to edit the active status of
    certification section. It returns the new active status of the section. 
    """

    status = True if request.POST['status'] == 'true' else False
    status = UserProfileService.edit_certification_status(request.user, status)
    return JsonResponse({'status': status})

@login_required
@csrf_exempt
def edit_skill(request):
    """This function handles user request to edit the skill content. It
    returns the edited content in json format. 
    """

    item_form = SkillItemForm(request.POST)
    item_id = request.POST['item_id']
    if item_form.is_valid():
        item = item_form.save(commit=False)
        item.id = item_id
        skill_item = UserProfileService.edit_skill_item(request.user, item)
    html = render_to_string('mycraze/item/skill.html', 
        {'item': skill_item, 'has_edit_permission': True})
    return HttpResponse(html)

def edit_skill_status(request):
    """This function handles user request to edit the active status of
    skill section. It returns the new active status of the section. 
    """

    status = True if request.POST['status'] == 'true' else False
    status = UserProfileService.edit_skill_status(request.user, status)
    return JsonResponse({'status': status})

@login_required
@csrf_exempt
def edit_course(request):
    """This function handles user request to edit the course content. It
    returns the edited content in json format. 
    """

    item_form = CourseItemForm(request.POST)
    item_id = request.POST['item_id']
    if item_form.is_valid():
        item = item_form.save(commit=False)
        item.id = item_id
        course_item = UserProfileService.edit_course_item(request.user, item)
    html = render_to_string('mycraze/item/course.html', 
        {'item': course_item, 'has_edit_permission': True})
    return HttpResponse(html)

def edit_course_status(request):
    """This function handles user request to edit the active status of
    course section. It returns the new active status of the section. 
    """

    status = True if request.POST['status'] == 'true' else False
    status = UserProfileService.edit_course_status(request.user, status)
    return JsonResponse({'status': status})

@login_required
@csrf_exempt
def edit_award(request):
    """This function handles user request to edit the award content. It
    returns the edited content in json format. 
    """

    item_form = AwardItemForm(request.POST)
    item_id = request.POST['item_id']
    if item_form.is_valid():
        item = item_form.save(commit=False)
        item.id = item_id
        award_item = UserProfileService.edit_award_item(request.user, item)
    html = render_to_string('mycraze/item/award.html', 
        {'item': award_item, 'has_edit_permission': True})
    return HttpResponse(html)

def edit_award_status(request):
    """This function handles user request to edit the active status of
    award section. It returns the new active status of the section. 
    """

    status = True if request.POST['status'] == 'true' else False
    status = UserProfileService.edit_award_status(request.user, status)
    return JsonResponse({'status': status})

@login_required
@csrf_exempt
def edit_language(request):
    """This function handles user request to edit the language content. It
    returns the edited content in json format. 
    """

    item_form = LanguageItemForm(request.POST)
    item_id = request.POST['item_id']
    if item_form.is_valid():
        item = item_form.save(commit=False)
        item.id = item_id
        language_item = UserProfileService.edit_language_item(request.user, item)
    html = render_to_string('mycraze/item/language.html', 
        {'item': language_item, 'has_edit_permission': True})
    return HttpResponse(html)

def edit_language_status(request):
    """This function handles user request to edit the active status of
    language section. It returns the new active status of the section. 
    """

    status = True if request.POST['status'] == 'true' else False
    status = UserProfileService.edit_language_status(request.user, status)
    return JsonResponse({'status': status})

@login_required
def edit_contact(request):
    """This function handles user request to edit the contact content. It
    returns the edited content in json format. 
    """

    section_form = ContactSectionForm(request.POST)
    if section_form.is_valid():
        section = section_form.save(commit=False)
        contact_section = UserProfileService.edit_contact_content(request.user, section)
    return JsonResponse({'personal_email': contact_section.personal_email, "phone_number": contact_section.phone_number})

def edit_contact_status(request):
    """This function handles user request to edit the active status of
    contact section. It returns the new active status of the section. 
    """

    status = True if request.POST['status'] == 'true' else False
    status = UserProfileService.edit_contact_status(request.user, status)
    return JsonResponse({'status': status})

@login_required
def get_stackoverflow_profiles(request):
    """This function handles user request to return a list of stackoverflow
    profiles attached by the user to his account. The response is in json
    format. 
    """

    user_id = int(request.GET['userId'])
    user = User.objects.get(id=user_id)
    stackoverflow_profile_list = user.social_auth.filter(provider='stackoverflow')
    data = serializers.serialize('json', stackoverflow_profile_list)
    return HttpResponse(data, mimetype="application/json")