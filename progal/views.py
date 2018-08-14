
from django.http import HttpResponse
from django.shortcuts import render


def welcome(request):
	title = 'Home'
	data = {
		'title' : title
	}
	return render(request, 'welcome.html', data)