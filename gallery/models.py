
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

class Gallery(models.Model):
	name = models.CharField(max_length = 100)
	category = models.CharField(max_length = 100)
	slug = models.SlugField()
	image = models.ImageField(default = 'default.png', blank = True)
	date = models.DateTimeField(auto_now_add = True)
	user = models.ForeignKey(User, default = None)
