"""This module contains view classe to receive user ping on the app."""

__author__ = "Srikrishnan Suresh"
__copyright__ = "Copyright 2015, MyCraze"
__version__ = "1.0.1"

from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
@login_required
def get_template_page(request):
	"""This function returns a ping, to indicate the app is healthy. 
    """
	context = {'message': 'The site is healthy'}
	return render(request, 'mycraze/template.html', context)
