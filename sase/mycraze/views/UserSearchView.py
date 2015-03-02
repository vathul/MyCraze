from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from mycraze.models.user.profile import UserProfile

@login_required
def get_users_page(request):
    context = {
        'image_url': settings.PROFILE_IMAGES_URL,
        'user_list': UserProfile.objects.all()
    }
    return render(request, 'mycraze/users.html',context)