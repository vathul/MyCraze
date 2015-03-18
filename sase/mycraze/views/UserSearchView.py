from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from mycraze.services.user import UserProfileService
from mycraze.services.search import UserSearchService

@login_required
def get_users_page(request):
    if not UserProfileService.has_user_profile(request.user):
        return HttpResponseRedirect('/mycraze/profile-complete/')
    criteria=None
    q=None
    if request.GET.get('criteria'):
        criteria=request.GET.get('criteria')
    else:
        return HttpResponseRedirect("/mycraze/users/?criteria=all")
    if request.GET.get('q'):
        q=request.GET.get('q')
    
    user_list = None    
    if criteria == 'all':
        user_list=UserSearchService.get_all_users(q)
    elif criteria == 'people':
        user_list=UserSearchService.get_users_by_name(q)
    elif criteria == 'skill':
        user_list=UserSearchService.get_users_by_skills(q)
    context = {
        'image_url': settings.PROFILE_IMAGES_URL,
        'query': q,
        'criteria': criteria,
        'user_list': user_list
    }
    return render(request, 'mycraze/users.html',context)