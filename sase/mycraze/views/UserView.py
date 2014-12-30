from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def get_resume_page(request):
	return render(request, 'mycraze/user-resume.html')