from django.shortcuts import render

# Create your views here.

def get_resume_page(request):
	return render(request, 'mycraze/user-resume.html')