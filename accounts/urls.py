
from django.conf.urls import url, include
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^gallery-register/$', views.gallery_register, name = 'gallery_register'),
    url(r'^gallery-login/', views.gallery_login, name = 'gallery_login'),
    url(r'^gallery-logout/', views.gallery_logout, name = 'gallery_logout'),
]
