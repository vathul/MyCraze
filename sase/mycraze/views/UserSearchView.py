from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from mycraze.models.user.profile import UserProfile

@login_required
def get_users_page(request):
    criteria=""
    q=""
    if request.GET.get('criteria'):
        criteria=request.GET.get('criteria')
    else:
        return HttpResponseRedirect("/mycraze/users/?criteria=all")
    if request.GET.get('q'):
        q=request.GET.get('q')
        
    
    context = {
        'image_url': settings.PROFILE_IMAGES_URL,
        'user_list': UserProfile.objects.all()
    }
    return render(request, 'mycraze/users.html',context)