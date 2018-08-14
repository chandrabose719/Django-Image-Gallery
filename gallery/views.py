
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Gallery
from . import forms
from django.contrib.auth.decorators import login_required

@login_required(login_url = '/account/gallery-login')
def all_images(request):
	title = 'Gallery'
	all_images = Gallery.objects.all().filter(user = request.user)
	data = {
		'title' : title,
		'all_images' : all_images
	}
	return render(request, 'gallery/all_images.html', data)


@login_required(login_url = '/account/gallery-login')
def new_gallery(request):
	title = 'New Gallery'
	if request.method == "POST":
		form = forms.createGalleryForm(request.POST, request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			instance.save()
			return redirect('gallery:all_images')
	else:
		form = forms.createGalleryForm()	
	data = {
		'title' : title,
		'form' : form
	}
	return render(request, 'gallery/new_gallery.html', data)	

