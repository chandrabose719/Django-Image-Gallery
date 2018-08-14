
from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = 'gallery'

urlpatterns = [
    url(r'^$', views.all_images, name = 'all_images'),    
    url(r'^new-gallery/$', views.new_gallery, name = 'new_gallery'),    
]
