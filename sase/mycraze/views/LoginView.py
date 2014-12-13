from django.shortcuts import render

# Create your login views here.

def get_login_page(request):
	return render(request, 'mycraze/sign-up.html')
