from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
@login_required
def get_template_page(request):
	context = {'message': 'The site is healthy'}
	return render(request, 'mycraze/template.html', context)
