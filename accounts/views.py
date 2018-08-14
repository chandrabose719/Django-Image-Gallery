
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def gallery_register(request):
	title = 'User Register'
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('accounts:gallery_login')
	else:
		form = UserCreationForm()
	data = {
		'title' : title,
		'form' : form
	}
	return render(request, 'accounts/gallery_register.html', data)			

def gallery_login(request):
	title = 'User Login'
	if request.method == 'POST':
		form = AuthenticationForm(data = request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
		return redirect('gallery:all_images')
	else:
		form = AuthenticationForm()
	data = {
		'title' : title,
		'form' : form
	}
	return render(request, 'accounts/gallery_login.html', data)			 

def gallery_logout(request):
	logout(request)
	return redirect('accounts:gallery_login')
