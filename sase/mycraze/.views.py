from django.shortcuts import render


# Create your views here.
def test(request):
	context = {'message': 'The site is healthy'}
	return render(request, 'mycraze/test.html', context)