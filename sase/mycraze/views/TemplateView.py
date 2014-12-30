from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def get_template_page(request):
	context = {'message': 'The site is healthy'}
	return render(request, 'mycraze/template.html', context)
