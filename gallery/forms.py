from django import forms
from . import models

class createGalleryForm(forms.ModelForm):
	class Meta:
		model = models.Gallery
		fields = ['name','category','slug','image']